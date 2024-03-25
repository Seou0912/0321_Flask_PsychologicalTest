from psypro.database import db
from datetime import datetime


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, nullable=False)
    k_answer = db.Column(db.String(100), nullable=False)
    participant_id = db.Column(
        db.Integer, db.ForeignKey("participant.id"), nullable=False
    )
