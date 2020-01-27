import env
from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    SECRET_KEY = env.APP_SECRET_KEY,
)

@app.route('/', methods=['GET'])
def home():
    data = {}
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
