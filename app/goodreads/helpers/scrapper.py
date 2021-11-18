from flask import Blueprint, url_for, jsonify, make_response, request
import requests
import json


def get_movie_by_title(title):
    pass


def get_movie_by_id(_id):
    pass


def get_book_reviews(title, limit='20', offset='0'):
    headers = {'Accept': 'application/json'}
    res = requests.get(url='https://www.goodreads.com/book/title.FORMAT',
                       headers=headers)
    print(res)


if __name__ == '__main__':
    get_book_reviews('Harry Potter')
