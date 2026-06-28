from datetime import datetime, timezone
from decimal import Decimal

from .extensions import db


class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    deposit = db.Column(db.DECIMAL(10, 2), nullable=False, default=Decimal("0.00"))
    account_value = db.Column(db.DECIMAL(10, 2), nullable=False, default=Decimal("0.00"))
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    def __repr__(self):
        return (
            f"<Entry "
            f"name={self.name!r} "
            f"deposit={self.deposit} "
            f"account_value={self.account_value} "
            f"created_at={self.created_at}>"
        )