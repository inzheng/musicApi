from flask import request
from flask import jsonify
from app.models import Music
from app import app

@app.route('/')
def index():
        musicList = Music.query.all()
        outputs = []
        for music in musicList:
            music_data = {'id': music.id,
                          'name': music.name,
                          'duration': music.duration,
                          'artist' : music.artist,
                          'genre' : music.genre}
            outputs.append(music_data)
        return jsonify(music = outputs)

# "/music" api is for reading all music information
@app.route('/music', methods = ['GET', 'POST'])
def music():
        if request.method == 'GET':
            musicList = Music.query.all()
            output = []
            for music in musicList:
                music_data = {'id': music.id,
                              'names': music.name,
                              'duration': music.duration,
                              'artists': music.artist,
                              'genres': music.genre}
                output.append(music_data)
            return jsonify(music = output)

        if request.method == 'POST':
            music = Music(name=request.json['name'],
                          artist=request.json['artist'],
                          genre=request.json['genre'],
                          duration=request.json['duration'])
            db.session.add(music)
            db.session.commit()
            return {'id' : music.id}

# "/music/<id>" api is for reading the music by id number
@app.route('/music/id/<id>', methods = ['GET', 'DELETE'])
def music_by_id(id):
    if request.method == 'GET':
        musicList = Music.query.get_or_404(id)
        return jsonify(name = musicList.name,
                       artist = musicList.artist,
                       genre = musicList.genre,
                       duration = musicList.duration)
    if request.method == 'DELETE':
        music = Music.query.get(id)
        if music is None:
            return {'error' : 'not found'}
        db.session.delete(music)
        db.session.commit()
        return { id : 'is deleted'}

# "/music/<music_name>" api is for reading the music by id number
@app.route('/music/names/<name>')
def music_by_name(name):
    musicList = Music.query.filter_by(name=name).first()
    #TODO: adding the condition if the same music name for multiple muisc
    return jsonify(name = musicList.name,
                   id = musicList.id,
                   artist = musicList.artist,
                   genre = musicList.genre,
                   duration = musicList.duration)


# "/music/<music_name>" api is for reading the music by id number
@app.route('/music/artists/<artist>')
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
    return {artist : output}

# "/music/<music_name>" api is for reading the music by id number
@app.route('/music/genres/<genre>')
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

# coding below is the delete api and reorder the sequence of the database
# # "/music/<music_name>" api is for deleting a music by id
# @app.route('/music/delete/<id>', methods = ['DELETE'])
# def delete_music_by_id(id):
#     music = Music.query.get(id)
#     if music is None:
#         return {'error' : 'not found '}
#     db.session.delete(music)
#     db.session.commit()
#     #reorder the id
#     db.session.execute("ALTER SEQUENCE music_id_seq RESTART WITH 1;")
#     db.session.execute("UPDATE music SET id = DEFAULT;")
#     db.session.commit()
#     return {id : "is deleted"}
