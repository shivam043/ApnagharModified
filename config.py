import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('jain.aman881@gmail.com')
MAIL_PASSWORD = os.environ.get('Maddy@1008')


# administrator list
ADMINS = ['jain.aman881@gmail.com','shivam043@gmail.com','amanzean@gmail.com']


class Auth:
    CLIENT_ID = ('688061596571-3c13n0uho6qe34hjqj2apincmqk86ddj'
                 '.apps.googleusercontent.com')
    CLIENT_SECRET = 'JXf7Ic_jfCam1S7lBJalDyPZ'
    REDIRECT_URI = 'https://localhost:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'

GOOGLE_LOGIN_CLIENT_ID = "559266694192-2a9o9hb8h0fv5juotg4apq25cff09mqb.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "MYOCAGDUraH_2Pkdo5BjeLnN"	
	
OAUTH_CREDENTIALS= {
    'facebook': {
        'id': '142985796160190',
        'secret': '1f63f0a9b205afa22cb26ffce63927a2'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    },
	'google': {
            'id': GOOGLE_LOGIN_CLIENT_ID,
            'secret': GOOGLE_LOGIN_CLIENT_SECRET
    }
}

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



