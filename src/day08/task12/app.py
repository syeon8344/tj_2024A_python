# day08 > task12 > app.py
from flask import Flask
from flask_cors import CORS
from controller import *

app = Flask(__name__)
CORS(app)


if __name__ == "__main__":
    app.run()