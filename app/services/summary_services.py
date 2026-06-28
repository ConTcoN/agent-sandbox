from app.models import Entry
from app.config import PERSONS
from app.extensions import db


def get_person_summary():
    summaries = []

    for name in PERSONS:
        latest_entry = (
            Entry.query
            .filter_by(name=name)
            .order_by(Entry.created_at.desc())
            .first()
        )

        account_value = latest_entry.account_value if latest_entry else 0

        deposit_sum = (
            db.session.query(db.func.sum(Entry.deposit))
            .filter_by(name=name)
            .scalar()
            or 0
        )

        summaries.append({
            "name": name,
            "account_value": account_value,
            "deposit_sum": deposit_sum,
            "profit": account_value - deposit_sum,
            "last_activity": latest_entry.created_at if latest_entry else None,
        })

    return summaries