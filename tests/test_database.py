from decimal import Decimal

from app.extensions import db
from app.models import Entry


def test_create_entry(app):
    with app.app_context():
        entry = Entry(
            name="Peter",
            deposit=Decimal("10.00"),
            account_value=Decimal("35.40"),
        )

        db.session.add(entry)
        db.session.commit()

        entry = Entry.query.one()

        assert entry.name == "Peter"
        assert entry.deposit == Decimal("10.00")
        assert entry.account_value == Decimal("35.40")
        assert entry.created_at is not None