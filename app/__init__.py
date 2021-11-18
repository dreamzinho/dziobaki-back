from flask import Flask
from app.config import Config
from app.imdb.controllers import imdb
from app.goodreads.controllers import goodreads

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(imdb)
app.register_blueprint(goodreads)
