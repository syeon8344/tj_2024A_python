# day08 > task12 > controller.py
from app import app
import service

@app.route("/getall")
def getall():
    service.getall()
