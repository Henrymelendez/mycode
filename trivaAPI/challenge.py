#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
import requests
import random

app = Flask(__name__)

API = "https://opentdb.com/api.php?amount=1&category=10&difficulty=easy&type=multiple"
DATA = {}
CORRECT = ""
def getQuestion():
    global DATA
    DATA = requests.get(API).json()
    results = DATA["results"]
    question = ""

    for i in results:
        question = i["question"]

    return question


def getAnswers():

    answers = []

    for qna in DATA["results"]:
        answers.append(qna["correct_answer"])
        CORRECT = qna["correct_answer"]
        for i in qna["incorrect_answers"]:
            answers.append(i)
    answer = random.shuffle(answers)
    return answers


@app.route("/")
def index():
    question = getQuestion()
    answers = getAnswers()

    return render_template("home.html",question=question, answers=answers)    

@app.route("/correct", methods=["POST"])
def success():
    global DATA
    correct = ""

    for a in DATA["results"]:
        correct = a["correct_answer"]

    selected_answer = request.form.getlist("answer")
    
    if request.method == "POST":
        print(request.form["answer"])
        print(correct)
        if request.form["answer"] == correct:
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("fail"))

@app.route("/fail")
def fail():
    return render_template("fail.html")

@app.route("/correct")
def correct():
    return render_template("correct.html")

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=2224)
