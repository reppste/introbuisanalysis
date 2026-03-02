from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>We should get to this landing page</h1>'

if __name__ == '__main__':
    app.run()