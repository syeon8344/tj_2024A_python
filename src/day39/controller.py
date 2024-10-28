import json

from app import app
from service import *
from flask import request, jsonify


@app.route("/chat" , methods=['get']) # http://localhost:5000/qooqoo
def get_answer():
    text = request.args.get('text', '')
    print(text)
    result = main(text)
    print(result)
    return jsonify(result)

