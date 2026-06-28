from app.extensions import db
from app.models import Entry
from app.services.summary_services import get_person_summary


def test_get_person_summary(app):
    with app.app_context():
        # Arrange
        db.session.add_all([
            Entry(name="Peter", deposit=100, account_value=120),
            Entry(name="Peter", deposit=50, account_value=180),
        ])
        db.session.commit()

        # Act
        result = get_person_summary()

        # Assert
        peter = next(r for r in result if r["name"] == "Peter")

        assert peter["account_value"] == 180
        assert peter["deposit_sum"] == 150
        assert peter["profit"] == 30