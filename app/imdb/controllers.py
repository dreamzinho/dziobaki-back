from flask import Blueprint, url_for, jsonify, make_response, request
import json
import helpers.scrapper as scrapper

imdb = Blueprint('imdb', __name__, url_prefix='/imdb')


@imdb.route('/sentiment/', methods=['GET'])
def get_movie_sentiment():
    """
    :return: Reviews sentiment for movie all/top5/worst5
    """
    data = request.get_json()
    title = data['title']
    review_type = data['review_type']
    if review_type == 'user_reviews':
        reviews = scrapper.get_user_reviews(title, 20)
        # get sentiment for reviews[]

    elif review_type == 'metacritic_reviews':
        reviews = scrapper.get_metacritic_reviews(title, 20)
        # get sentiment for reviews[]

    return None
