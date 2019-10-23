import csv
from flask import Flask, render_template, redirect, url_for, flash, make_response, session,  request, jsonify, json,jsonify
import random, copy
from random import shuffle
from random import sample
import os, time, datetime
import io
import questions as qm
from questions import*

app = Flask(__name__)
app.secret_key = os.urandom(24)

def shuffle(q):
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(list(q))
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i + 1
        return selected_keys


@app.route('/phishing', methods=['GET', 'POST'])
def phishing():
    with open('TemplateQuiz.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        quiz = list(reader)
   
        question =quiz[current_question_index][0]
        options = quiz[current_question_index][1:-1]
        correct_answer = quiz[current_question_index][-1]
        current_question = phishings()
        current_answer = request.form.get('i')
        for i in question:
            answered = request.form.get(i)
            if i[0] == answered:
                question["correct"].append(str(int(session[current_question_index])))
            #else:
             #   questions["wrong"].append(str(int(session[current_question_index])))
            
        #session[current_question_index] = session[current_question_index]+1

   
    
    if "current_question" not in session:
        session["current_question"] = "1"

    currentN=int(session["current_question"])
    currentQ = random.choice(quiz)
    question_shuffled= shuffle(quiz)
    app.nquestions = len(quiz)
    return render_template('socials.html', q=question_shuffled, o=question, num=currentN, ntot=app.nquestions)

if __name__ == '__main__':
    app.run(debug=True)

