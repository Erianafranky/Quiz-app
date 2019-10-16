import csv
from flask import Flask, render_template, redirect, url_for, flash, make_response, session,  request, jsonify, json,jsonify
import random, copy
from random import shuffle
from random import sample
import os, time, datetime
from questions import*

app = Flask(__name__)
app.secret_key = os.urandom(24)



@app.route('/social', methods=['GET', 'POST'])
def social():
    with open('TemplateQuiz.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print (row)            
            quiz = list(reader)  
    q = random.choice(quiz)
    
    if "current_question" not in session:
        session["current_question"] = "1"

    elif session["current_question"] not in quiz:
        questions["wrong"] = list(set(questions["wrong"]))
        questions["correct"] = list(set(questions["correct"]))
    currentN=int(session["current_question"])
    currentQ = random.choice(quiz)

    app.nquestions = len(quiz)
   

    return render_template('socials.html', num=currentN, ntot=app.nquestions, question=currentQ)

if __name__ == '__main__':
    app.run(debug=True)