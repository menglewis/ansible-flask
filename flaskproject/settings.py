import os


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(APP_DIR, 'test.sqlite')
    DEBUG = True


class ProdConfig(Config):
    '''Production configuration.'''
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@localhost/flaskproject".format(os.environ['DATABASE_USER'],
                                                                                   os.environ['DATABASE_PASSWORD'])
    DEBUG = False


class DevConfig(Config):
    '''Development configuration.'''
    SECRET_KEY = 'devsecretkey'
    SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@localhost/flaskproject".format(os.environ['DATABASE_USER'],
                                                                                   os.environ['DATABASE_PASSWORD'])


class TestingConfig(Config):
    SECRET_KEY = 'testsecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False
