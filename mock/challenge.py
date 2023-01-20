#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from decouple import config
from datetime import date
import requests

api_key = config("API_KEY", default="aaedd575ad2c4cfe8ae50c5553872db7")

today = date.today()
date_string = today.strftime("%Y=%m-%d")
API = f"https://newsapi.org/v2/everything?q=Apple&from={date_string}&sortBy=popularity&apiKey={api_key}"

DATA = {}
ARTS = []
app=Flask(__name__)


@app.route("/")
def index():
    global DATA
    DATA = requests.get(API).json()
    DATA =  DATA["articles"]
    titles = []
    for articles in DATA:
        ARTS.append(articles)

    return render_template("home.html",titles=ARTS)

app.route("/article/<titles>", methods=["GET","POST"])
def getarticle(titles):
    content = ""
    titles = request.args.get("title")
    print(titles)
    for title in DATA:
        print(title)
        
    return "No Article"



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2224)


