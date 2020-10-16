import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

class DatabaseURI:

    # Just change the names of your database and crendtials and all to connect to your local system
    DATABASE_NAME = "fyyur"
    username = 'postgres'
    password = ''
    url = '127.0.0.1:5432'
    SQLALCHEMY_DATABASE_URI = "postgres://{}:{}@{}/{}".format(
        username, password, url, DATABASE_NAME)


# TODO. IMPLEMENT DATABASE URL
# //username:password@server/db
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False