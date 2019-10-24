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



@app.route('/phishing', methods=['GET', 'POST'])
    
def phishing():
    with open('TemplateQuiz.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        quiz = list(reader)
        random.shuffle(quiz)
    if request.method == 'POST':
        questions_file = 'TemplateQuiz .csv'
        question = quiz[current_question_index][0]
        options = quiz[current_question_index][1:-1]
        correct_answer = quiz[current_question_index][-1]
        entered_answer =request.form.get('answer_phishing')
        if not entered_answer:
            flash("Please choose an answer", "error")
        else:
            curr_answer = request.form['answer_phishing']
            correct_answer = quiz[current_question_index][-1]
        if curr_answer == correct_answer[:len(curr_answer)]:
            quiz["correct"].append(int([current_question_index]))
        else:
            quiz["wrong"].append(int([current_question_index]))
        
        session[current_question_index] = str(int(session[current_question_index])+1)
        quiz["curretq"] = max(int(session[current_question_index]), quiz["curretq"])
        
    if current_question_index not in session:
        session[current_question_index] = "1"

    elif session[current_question_index] not in qm:
        quiz["wrong"] = list(set(quiz["wrong"]))
        quiz["correct"] = list(set(quiz["correct"]))
        return render_template('end-quiz.html', question=quiz)
    currentN = int(session[current_question_index])
    currentQ = quiz[current_question_index][0]
    a1,a2,a3,a4 = quiz[current_question_index][1:-1]
    app.nquestions = len(quiz)
    return render_template('socials.html', num=currentN, ntot=app.nquestions, question=currentQ, ans1=a1,ans2=a2,ans3=a3,ans4=a4)






if __name__ == '__main__':
    app.run(debug=True)