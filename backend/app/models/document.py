from . import db
from datetime import datetime, timezone

class Document(db.Model):
    # id means that this is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # title is a string that must not be null
    title = db.Column(db.String(100), nullable=False)
    # content is a text field that can be empty 
    content = db.Column(db.Text, nullable=True)
    # created_at is a timestamp that defaults to the current time
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'<Document {self.title}>'