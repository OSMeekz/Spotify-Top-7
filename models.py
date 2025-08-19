#from server import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
#from dotenv import load_dotenv

#load_dotenv()

db = SQLAlchemy()

"""Based off of original data table"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spotify_user_id = db.Column(db.String, unique=True, nullable=False)
     #going to utilize Spotify ID from the API
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spotify_track_id = db.Column(db.String, unique=True, nullable=False)
    #gathering this data from Spotify as well 
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    album = db.Column(db.String)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

class UserFavorite(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id', ondelete='CASCADE'), nullable=False)
    position = db.Column(db.SmallInteger, primary_key=True)  # 1–7
    selected_at = db.Column(db.DateTime, default=datetime.utcnow)

    # optional relationship helpers
    user = db.relationship('User', backref='favorites')
    song = db.relationship('Song')

#def connect_to_db(app, db_name, echo=True):
    #"""Connect to database."""

   # app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
   # app.config["SQLALCHEMY_ECHO"] = True
   # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

   # db.app = app
   # db.init_app(app)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///Top7", echo=True):
    """Connect to database."""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == "__main__":
    from server import app
    connect_to_db(app,)
    #connect_to_db(app, "")
    
    app.app_context().push()