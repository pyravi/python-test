from app import db

class Song(db.Model):
    """
    Create an Song table
    """
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    duration = models.DurationField(_("Duration in seconds "),index=True)
    timestamp = models.TimeField(_("Date"), auto_now=False, auto_now_add=False)

class Podcast(db.Model):
    """
    Create an Podcast table
    """
    __tablename__ = 'podcast'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    duration = models.DurationField(_("Duration in seconds "),index=True)
    host = db.Column(db.String(100), index=True)
    timestamp = models.TimeField(_("Date"), auto_now=False, auto_now_add=False)
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
    duration = models.DurationField(_("Duration in seconds "),index=True)
    timestamp = models.TimeField(_("Date"), auto_now=False, auto_now_add=False)
   