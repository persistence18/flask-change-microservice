from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

def checkList(stock):
    stock = stock.upper()
    restrictStock = ["IBM", "AAPL", "GOOG", "MSFT", "AMZN", "JPM"]
    if stock in restrictStock:
        return "Rejected: Restricted Stock"
    return "Approved"

@app.route('/')
def hello():
    """Return a Mock Response to a trade rule request."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /tradeRule'


@app.route('/checkTrade', methods=['GET'])
def checkTrade():
    stock = request.args.get('stock')
    date = request.args.get('date')
    # return jsonify({"stock": stock, "date": date})
    return jsonify({"trade Request: ": checkList(stock)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
