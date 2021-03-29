from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import os


app = Flask('__name__')

EVN = 'con'
if EVN == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xuboyang:xby1999726@localhost/music'
else:
    app.debug = False
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fdibzjsbduhpza:9d2578d4965857b08f9da8e82d4d0888654403d5d89155284c46775efe131ef4@ec2-54-211-176-156.compute-1.amazonaws.com:5432/dc58roq6bsu8n8'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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



@app.route('/')
def index():
        musicList = Music.query.all()
        output = []
        for music in musicList:
            music_data = {'id': music.id,
                          'name': music.name,
                          'duration': music.duration,
                          'artist' : music.artist,
                          'genre' : music.genre}
            output.append(music_data)
        return jsonify(music = output)

# "/music" api is for reading all music information
@app.route('/music')
def get_music():
        musicList = Music.query.all()
        output = []
        for music in musicList:
            music_data = {'id': music.id,
                          'name': music.name,
                          'duration': music.duration,
                          'artist': music.artist,
                          'genre': music.genre}
            output.append(music_data)
        return jsonify(music = output)

# "/music/<id>" api is for reading the music by id number
@app.route('/music/<id>')
def get_music_by_id(id):
    musicList = Music.query.get_or_404(id)
    return jsonify(name = musicList.name,
                   artist = musicList.artist,
                   genre = musicList.genre,
                   duration = musicList.duration)


# "/music/<music_name>" api is for reading the music by id number
@app.route('/music/name/<name>')
def get_music_by_name(name):
    musicList = Music.query.filter_by(name=name).first()
    #TODO: adding the condition if the same music name for multiple muisc
    return jsonify(name = musicList.name,
                   id = musicList.id,
                   artist = musicList.artist,
                   genre = musicList.genre,
                   duration = musicList.duration)

# "/music/<music_name>" api is for reading the music by id number
@app.route('/music/artist/<artist>')
def get_music_by_artist(artist):
    musicList = Music.query.filter_by(artist=artist).all()
    # TODO: adding the condition if the same music name for multiple muisc
    output = []
    for music in musicList:
        music_data = {"id" : music.id,
                      "name" : music.name,
                      "genre" : music.genre,
                      "duration" : music.duration}
        output.append(music_data)
    return jsonify(artist = output)

# "/music/<music_name>" api is for reading the music by id number
@app.route('/music/genre/<genre>')
def get_music_by_genre(genre):
    musicList = Music.query.filter_by(genre=genre).all()
    output = []
    for music in musicList:
        music_data = {"id" : music.id,
                      "name" : music.name,
                      "artist" : music.artist,
                      "duration" : music.duration}
        output.append(music_data)
    return {genre: output}

# "/music/<music_name>" api is for reading the music by id number
@app.route('/music/duration/<duration>')
def get_music_by_duration(duration):
    musicList = Music.query.filter_by(duration=duration).all()
    output = []
    for music in musicList:
        music_data = {"id" : music.id,
                      "name" : music.name,
                      "artist" : music.artist,
                      "genre" : music.genre}
        output.append(music_data)
    title = 'duration is ' + duration
    return {title: output}

# "/music/<music_name>" api is for adding a new music
@app.route('/music/add', methods = ['POST'])
def add_music():
       music = Music(name=request.json['name'],
                     artist=request.json['artist'],
                     genre=request.json['genre'],
                     duration=request.json['duration'])
       db.session.add(music)
       db.session.commit()
       return {'id' : music.id}

# "/music/<music_name>" api is for deleting a music by id
@app.route('/music/delete/<id>', methods = ['DELETE'])
def delete_music_by_id(id):
    music = Music.query.get(id)
    if music is None:
        return {'error' : 'not found '}
    db.session.delete(music)
    db.session.commit()
    #reorder the id
    db.session.execute("ALTER SEQUENCE music_id_seq RESTART WITH 1;")
    db.session.execute("UPDATE music SET id = DEFAULT;")
    db.session.commit()
    return {id : "is deleted"}

if __name__ == "__main__":
    app.run()
