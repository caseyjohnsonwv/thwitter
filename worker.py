import re
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

def make_thread(text, preserve_whitespace=False):
    """
    text: str
    return: List[str]
    """
    thread = []
    tweet = ""
    punc = "([\.\-,;:\s!\?]+)"
    if not preserve_whitespace:
        text = re.sub('\s+',' ',text)
    words = re.split(punc, text)
    i,j,breakpoint = 0,0,0
    while i < len(words):
        #record for frequent use
        j = len(tweet)
        # record punctuation marks as tweet breakpoints
        if re.match(punc, words[i]):
            breakpoint = j + len(words[i]) + 1
        # add word to tweet if length permits
        if j + len(words[i]) < 240:
            tweet += words[i]
        # tweet is full - try to break at last punctuation
        elif breakpoint > 0:
            tweet = tweet[:breakpoint]
            thread.append(tweet)
            tweet = words[i]
            breakpoint = 0
        # no previous punctuation - break with elipsis mid-word
        else:
            tweet += words[i]
            while len(tweet) > 240:
                tweet,overflow = tweet[:237],tweet[237:]
                tweet += "..."
                thread.append(tweet)
                tweet = "..." + overflow
        #next word
        i += 1
    # append leftovers to thread
    thread.append(tweet)
    # strip ending whitespaces
    if not preserve_whitespace:
        thread = [tweet.strip() for tweet in thread]
    return thread
