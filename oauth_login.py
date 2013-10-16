import twitter

'''Oauth Login Authentication:
Function expecting Twitter Developer to include four important parameters'''


def oauth_login():
    CONSUMER_KEY = 'H4mvOwPb2C0wqdWA8aQU6g'
    CONSUMER_SECRET = 'rwnpyM24aMguzo3a62AjmXQ7hMYf4ELmfVJIyMZo'
    OAUTH_TOKEN = '17129715-55udyt3pBlcojpFGQa3Iet10tLWu1OQTf60dUWQLP'
    OAUTH_TOKEN_SECRET = 'mVsOTptPy5fzGVY8Qt7DVg5RVzscMlyoxJEi2rPSyk'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api
