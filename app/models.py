from app import db
from datetime import datetime

class Song(db.Model):
    """
    Create an Song table
    """
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    duration = db.Column(db.Integer, index=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class Podcast(db.Model):
    """
    Create an Podcast table
    """
    __tablename__ = 'podcast'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    duration = db.Column(db.Integer, index=False)
    host = db.Column(db.String(100), index=True)
    participants = db.Column(db.String(100), index=False)

class Audiobook(db.Model):
    """
    Create an Audiobook table
    """
    __tablename__ = 'audiobook'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    author_title = db.Column(db.String(100), index=True)
    narrator = db.Column(db.String(100), index=True)
    duration = db.Column(db.Integer, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
