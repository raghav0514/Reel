import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/reels.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'app/static/videos'
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}
