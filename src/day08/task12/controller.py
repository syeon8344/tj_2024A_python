# day08 > task12 > controller.py
from app import app
import service




@app.route("/getall" , methods = ["GET"])
def getall():
    return service.getall()

@app.route("/maxminlist" ,methods = ["GET"])
def maxminlist():
    return service.max_min_list()





@app.route("/toptransaction")
def top_ten_transaction():
    service.top_ten_transaction()

@app.route("/comparetransaction")
def compare_transaction():
    service.compare_transaction()

@app.route("/weekdaymost")
def weekday_most_transactions():
    service.weekday_most_transactions()