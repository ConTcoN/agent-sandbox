import os

PERSONS = [
    person.strip()
    for person in os.getenv(
        "PERSONS",
        "Peter,Paul,Maria,Julia",
    ).split(",")
]

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    "sqlite:////data/database.db"
)