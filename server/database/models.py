from email.policy import default
import imp
from unicodedata import name
from .db import db

class Note(db.Document):
    title = db.StringField(required=True, unique=True)
    description = db.StringField(required=True)
    priority = db.StringField(default="low")
    completed = db.BooleanField(default=False)
    archvied = db.BooleanField(default=False)

