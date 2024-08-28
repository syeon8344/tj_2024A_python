# day11 > task16 > controller.py
from app import app
import service
from flask import request

@app.route("/jobkorea")
def get_jobkorea():
    key = request.args.get("key")
    result = service.get_jobkorea(key)
    if service.list_to_csv(result):
        result_json = service.read_csv("잡코리아검색기록")
        return result_json

@app.route("/educationstats")
def get_education_stats():
    return service.get_education_stats()

@app.route("/experiencestats")
def get_experience_stats():
    return service.get_experience_stats()
