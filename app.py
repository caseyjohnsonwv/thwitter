import env
from worker import *
from flask import Flask, request, render_template

app = Flask(__name__)
app.config.update(
    SECRET_KEY = env.APP_SECRET_KEY,
)

@app.route('/', methods=['GET'])
def home():
    data = {}
    return render_template('index.html', data=data, page='index')

@app.route('/go', methods=['POST'])
def go():
    text = request.form.get("thread_content")
    preserve_whitespace = request.form.get("preserve_whitespace")
    tweets = make_thread(text, preserve_whitespace)
    data = {'tweets':tweets}
    return render_template('index.html', data=data, page='go')

if __name__ == "__main__":
    app.run()
