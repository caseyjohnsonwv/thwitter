import env
from oauth_logic import *
from twitter_thread import *
from flask import Flask, request, render_template, redirect, session

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
    url = initiate_oauth()
    return redirect(url)

@app.route('/callback', methods=['GET'])
def callback():
    url = oauth_callback()
    return redirect(url)

@app.route('/share', methods=['GET'])
def share():
    data = {}
    return render_template('index.html', data=data, page='share')

@app.route('/alive', methods=['GET'])
def alive():
    return "Alive"

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect("/home")

if __name__ == "__main__":
    app.run()
