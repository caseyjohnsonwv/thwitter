import env
import tweepy
from flask import session, request

def initiate_oauth():
    """
    return: str
    """
    try:
        session['AUTH_TOKEN']
        session['AUTH_TOKEN_SECRET']
        redirect_url = '/share'
    except Exception:
        auth = tweepy.OAuthHandler(env.TWITTER_API_KEY, env.TWITTER_API_SECRET, env.CALLBACK_URL)
        redirect_url = auth.get_authorization_url()
        session['REQUEST_TOKEN'] = auth.request_token
    return redirect_url

def oauth_callback():
    """
    return: str
    """
    auth = tweepy.OAuthHandler(env.TWITTER_API_KEY, env.TWITTER_API_SECRET)
    try:
        auth.request_token = session['REQUEST_TOKEN']
        verifier = request.args.get('oauth_verifier')
        auth.get_access_token(verifier)
        session['AUTH_TOKEN'],session['AUTH_TOKEN_SECRET'] = auth.access_token, auth.access_token_secret
        redirect_url = '/share'
    except Exception:
        redirect_url = '/'
    return redirect_url
