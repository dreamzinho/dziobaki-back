from flask import Blueprint, url_for, jsonify, make_response, request
import json

goodreads = Blueprint('goodreads', __name__, url_prefix='/goodreads')
