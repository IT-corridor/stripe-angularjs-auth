import os

DEBUG = True

TOKEN_SECRET = os.environ.get('SECRET_KEY') or 'JWT Token Secret String'
FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET') or '3c9a68e9d6a29b64g34g3f240112c7c6998b70'
GITHUB_SECRET = os.environ.get('GITHUB_SECRET') or 'GitHub Client Secret'
FOURSQUARE_SECRET = os.environ.get('FOURSQUARE_SECRET') or 'Foursquare Client Secret'
GOOGLE_SECRET = os.environ.get('GOOGLE_SECRET') or 'Google Client Secret'
LINKEDIN_SECRET = os.environ.get('LINKEDIN_SECRET') or 'LinkedIn Client Secret'
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY') or 'J6eeF1zgj7CmGGg3g34BO5ARPMPbrC'
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET') or 'OMcmHxnOBIg23g22g2R6VdIBshsznk25P6VpWTHfVyQBZ63JMaluGOLbsW'
TWITTER_CALLBACK_URL = os.environ.get('TWITTER_CALLBACK_URL') or '	http://127.0.0.1:3000/auth/twitter'
BITBUCKET_SECRET = os.environ.get('BITBUCKET_SECRET') or 'Bitbucket Client Secret'
STRIPE_API_KEY = 'sk_test_1AFSPD5Dg8RihyPPtylWiSsR'
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db'