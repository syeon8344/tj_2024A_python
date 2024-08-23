# day08 > app > app.py
from flask import Flask
app = Flask(__name__)

# controller 가져오기
from controller import *


if __name__ == "__main__":
    app.run()