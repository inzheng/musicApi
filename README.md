# musicApi
Introduction: This application build multiple rest api 


----------

"/" and "/music": read all information from the database

"/muisc/name/<name>":read all music by music name
  
"/muisc/artist/<artist>":read all music by artist
  
"/muisc/<id>":read all music by id
  
"/muisc/genre/<genre>":read all music by genre
  
"/muisc/duration/<duration>":read all music by duration
  
"/muisc/add": adding a music

"/muisc/delete/<id>": deleting a music by id 
  
  
-------
url: https://music-rest-api.herokuapp.com

------
Database information:  

music(table) with five columns: id, name, artist, genre, duration

list of names: lostrivers, badguy, Lovely, Wish you were, livemealone
list of artists: BillieEilish, xuboyang, PepiGensberg
list of genres: popular, electropop, trapop
durations includes: 3, 4, 5
