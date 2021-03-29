# musicApi
Introduction: This application build multiple rest api 

A music will conain the music name, artist, duration and genre
----------

"/" and "/music": read all information from the database

"/music/name/<name>":read all music by music name
  
"/music/artist/<artist>":read all music by artist
  
"/music/<id>":read all music by id
  
"/music/genre/<genre>":read all music by genre
  
"/music/duration/<duration>":read all music by duration
  
"/music/add": adding a music

"/music/delete/<id>": deleting a music by id 
  
  
-------
url: https://music-rest-api.herokuapp.com

------
Database information:  

music(table) with five columns: id, name, artist, genre, duration

list of names: lostrivers, badguy, Lovely, Wish you were, livemealone
list of artists: BillieEilish, xuboyang, PepiGensberg
list of genres: popular, electropop, trapop
durations includes: 3, 4, 5
