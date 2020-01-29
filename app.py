import env
from worker import *
from flask import Flask, request, render_template, redirect, session
import tweepy

app = Flask(__name__)
app.config.update(
    SECRET_KEY = env.APP_SECRET_KEY,
)

@app.route('/home', methods=['GET'])
def home():
    data = {}
    return render_template('index.html', data=data, page='home')

@app.route('/go', methods=['POST'])
def go():
    text = request.form.get("thread_content")
    preserve_whitespace = request.form.get("preserve_whitespace")
    tweets = make_thread(text, preserve_whitespace)
    data = {'tweets':tweets}
    return render_template('index.html', data=data, page='go')

@app.route('/auth', methods=['POST'])
def auth():
    try:
        session['AUTH_TOKEN']
        session['AUTH_TOKEN_SECRET']
        redirect_url = '/share'
    except Exception:
        auth = tweepy.OAuthHandler(env.TWITTER_API_KEY, env.TWITTER_API_SECRET, env.CALLBACK_URL)
        redirect_url = auth.get_authorization_url()
        session['REQUEST_TOKEN'] = auth.request_token
    finally:
        return redirect(redirect_url)

@app.route('/callback', methods=['GET'])
def callback():
    auth = tweepy.OAuthHandler(env.TWITTER_API_KEY, env.TWITTER_API_SECRET)
    try:
        auth.request_token = session['REQUEST_TOKEN']
        verifier = request.args.get('oauth_verifier')
        auth.get_access_token(verifier)
        session['AUTH_TOKEN'],session['AUTH_TOKEN_SECRET'] = auth.access_token, auth.access_token_secret
        redirect_url = '/share'
    except Exception:
        redirect_url = '/'
    finally:
        return redirect(redirect_url)

@app.route('/share', methods=['GET'])
def share():
    data = {}
    return render_template('index.html', data=data, page='share')

@app.route('/alive', methods=['GET'])
def alive():
    data = {}
    return render_template('index.html', data=data, page='alive')

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect("/home")

if __name__ == "__main__":
    app.run()
