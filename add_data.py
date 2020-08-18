#script to add test data
from app import db
from models import Song, Playlist, Item, User

p1 = Playlist(id = 3456)
p2 = Playlist(id = 2342)
p3 = Playlist(id = 4576)
p4 = Playlist(id = 8743)
u1 = User(id = 1, username = "mlky_way", playlist_id = p1.id)
u2 = User(id = 2, username = "martian2", playlist_id = p2.id)
u3 = User(id = 3, username = "andromeda_3", playlist_id = p3.id)
u4 = User(id = 4, username = "calypso123", playlist_id = p4.id)

s1 = Song(id = 1, artist = "Franks Sinatra", title = "Fly me to the Moon", n = 0)
s2 = Song(id = 2, artist = "David Bowie", title = "Space Oddity", n = 0)
s3 = Song(id = 3, artist = "Sting", title = "Walking on the Moon", n = 0)
s4 = Song(id = 4, artist = "Nick Cave & The Bad Seeds", title = "Rings of Saturn", n = 0) 
s5 = Song(id = 5, artist = "Babylon Zoo", title = "Spaceman", n = 0)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)
db.session.add(s5)
db.session.commit()
