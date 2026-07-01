from flask import Blueprint, redirect, render_template, request, url_for
from decimal import Decimal

from .extensions import db
from .models import Entry
from .config import PERSONS
from .services.summary_services import get_person_summary

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        deposit = Decimal(request.form["deposit"])
        account_value = Decimal(request.form["account_value"])

        if deposit < 0:
            return (
                render_template(
                    "index.html",
                    persons=PERSONS,
                    entries=get_entries(),
                    error="Der Einzahlbetrag darf nicht negativ sein.",
                ),
                400,
            )

        if account_value < 0:
            return (
                render_template(
                    "index.html",
                    persons=PERSONS,
                    entries=get_entries(),
                    error="Der Account-Wert darf nicht negativ sein.",
                ),
                400,
            )

        entry = Entry(
            name=request.form["name"],
            deposit=deposit,
            account_value=account_value,
        )

        db.session.add(entry)
        db.session.commit()

        return redirect("./")

    entries=get_entries()
    summaries = get_person_summary()

    return render_template(
        "index.html",
        persons=PERSONS,
        entries=entries,
        summaries=summaries,
    )

def get_entries():
    return Entry.query.order_by(Entry.created_at.desc()).all()