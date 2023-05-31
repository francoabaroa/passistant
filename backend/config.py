import os
from dotenv import load_dotenv

load_dotenv()
database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")

if not database_uri:
    raise Exception("SQLALCHEMY_DATABASE_URI is not set in the environment variables")

class Config(object):
    SQLALCHEMY_DATABASE_URI = database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False