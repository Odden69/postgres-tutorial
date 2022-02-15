from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the Artist Table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class-based model for the Album Table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class-based model for the Track Table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined below
session = Session()

base.metadata.create_all(db)

# Query 1 - select all records from the Artist table
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.ArtistId, artist.Name, sep= " | ")

# Query 2 - select only the name column from the Artist table
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.Name)

# Query 3 - select only Queen from the Artist table, (.first is optional)
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep= " | ")

# Query 4 - select only no 51 from the Artist table
# artist = session.query(Artist).filter_by(ArtistId="51").first()
# print(artist.ArtistId, artist.Name, sep= " | ")

# Query 5 - select only the albums from the Album table with ArtistId 51
albums = session.query(Album).filter_by(ArtistId="51")
for album in albums:
    print(album.AlbumId, album.ArtistId, album.Title, sep= " | ")
    
# Query 6 - select all tracks from the Track table with Composer Queen
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, 
    track.GenreId, track.Composer, track.Milliseconds, track.Bytes, 
    track.UnitPrice, sep= " | ")


