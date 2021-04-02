from app import db

class Music(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique=True)
    duration = db.Column(db.Integer, nullable = False)
    artist = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(50))

    def __init__(self, genre, name, duration, artist):
        self.genre = genre
        self.name = name
        self.duration = duration
        self.artist = artist

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.duration} - {self.artist} - {self.genre}"
