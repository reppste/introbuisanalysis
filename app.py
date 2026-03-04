from flask import Flask
from Configs.Queries import *
app = Flask(__name__)

@app.route('/')
def home():
    names = retrieve_names()

    page_contents = ""

    page_contents += f"<h1>{names}</h1><br>"
    return page_contents

if __name__ == '__main__':
    app.run()