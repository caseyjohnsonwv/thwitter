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
    text = request.get("THREAD_CONTENT")
    tweets = make_thread(text)
    data = {'tweets':tweets}
    return render_template('index.html', data=data, page='go')

if __name__ == "__main__":
    app.run()
