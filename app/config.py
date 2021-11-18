import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "71c7f3d1a35881f64fd4f68e5be368e121c27bbafe682fd33649641c47fa1be9"
