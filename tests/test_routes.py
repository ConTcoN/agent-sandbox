from decimal import Decimal

from app.config import PERSONS
from app.extensions import db
from app.models import Entry

def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hup Holland Hup" in response.data
    
def test_submit_entry(client, app):
    response = client.post(
        "/",
        data={
            "name": "Peter",
            "deposit": "10",
            "account_value": "35.40",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    with app.app_context():
        entry = Entry.query.one()

        assert entry.name == "Peter"
        assert entry.deposit == Decimal("10.00")
        assert entry.account_value == Decimal("35.40")
        assert entry.created_at is not None

def test_homepage_contains_persons(client):
    response = client.get("/")

    html = response.data.decode()

    for person in PERSONS:
        assert person in html

def test_homepage_shows_entries(client, app):
    with app.app_context():
        db.session.add(
            Entry(
                name="Peter",
                deposit=Decimal("12.50"),
                account_value=Decimal("100.00"),
            )
        )

        db.session.add(
            Entry(
                name="Maria",
                deposit=Decimal("8.00"),
                account_value=Decimal("108.00"),
            )
        )

        db.session.commit()

    response = client.get("/")

    html = response.data.decode()

    assert "Peter" in html
    assert "Maria" in html
    assert "12.50" in html
    assert "100.00" in html

    assert "8.00" in html
    assert "108.00" in html

def test_submit_entry_redirects(client):
    response = client.post(
        "/",
        data={
            "name": "Peter",
            "deposit": "10",
            "account_value": "35.40",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")

def test_submit_entry_rejects_negative_deposit(client, app):
    response = client.post(
        "/",
        data={
            "name": "Peter",
            "deposit": "-10",
            "account_value": "35.40",
        },
        follow_redirects=True,
    )

    assert response.status_code == 400

    with app.app_context():
        assert Entry.query.count() == 0

def test_submit_entry_rejects_negative_account_value(client, app):
    response = client.post(
        "/",
        data={
            "name": "Peter",
            "deposit": "10",
            "account_value": "-35.40",
        },
        follow_redirects=True,
    )

    assert response.status_code == 400

    with app.app_context():
        assert Entry.query.count() == 0