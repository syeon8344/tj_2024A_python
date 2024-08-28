# day11 > task16 > app.py
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from controller import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)