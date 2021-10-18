from logging import info
from flask import Flask, render_template, request
import requests

url = "http://data.fixer.io/api/latest?access_key=6fd37c9de68047775ff0c89f46071da0"

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")   #USD
        secondCurrency = request.form.get("secondCurrency") #TRY

        amount = request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)

        infos = response.json()
        
        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue / firstValue) * float(amount)

        currencyInfo = dict()

        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        app.logger.info(infos)

        return render_template("index.html", info = currencyInfo)
        
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

