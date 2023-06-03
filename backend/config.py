import os
from dotenv import load_dotenv

load_dotenv()
database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
secret_key = os.getenv("SECRET_KEY", "")

if not database_uri:
    raise Exception("SQLALCHEMY_DATABASE_URI is not set in the environment variables")

if not secret_key:
    raise Exception("SECRET_KEY is not set in the environment variables")

class Config(object):
    SECRET_KEY = secret_key
    SQLALCHEMY_DATABASE_URI = database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False