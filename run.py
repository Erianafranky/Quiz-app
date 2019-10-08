from flask import Flask, render_template, redirect, url_for, flash, make_response, session,  request, jsonify, json,jsonify
import random, copy
from random import shuffle
from random import sample
import os, time, datetime
from questions import*

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def home():
    return render_template('home.html')

"""
function which takes the keys of the
dictionary and shuffles them
"""
def shuffle(q):
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(list(q.keys()))
        #current_selection = random.sample(list(social_engs),3)
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i + 1
        return selected_keys


@app.route('/social', methods=['GET', 'POST'])
def social():
    if request.method == 'POST':
        correct = 0 
        for i in social_engs.keys():
            answered = request.form.get(i)
            if social_eng[i][0] == answered:
                #correct = correct + 1
                questions["correct"].append(int(session["current_question"]))
            else:
                questions["wrong"].append(int(session["current_question"]))
       #return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'      
   
            session["current_question"] = str(int(session["current_question"])+1)
            questions["curretq"] = max(int(session["current_question"]), questions["curretq"])
            if session["current_question"] in social_engs:
                redirect(url_for('social'))
            else:
                questions["wrong"]=list(set(questions["wrong"]))
                questions["correct"]=list(set(questions["correct"]))        
                return render_template('end-quiz.html', question=questions)
        #return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

    if "current_question" not in session:
        session["current_question"] = "1"
    elif session["current_question"] not in social_engs:
        questions["wrong"]=list(set(questions["wrong"]))
        questions["correct"]=list(set(questions["correct"]))
        #return render_template('end-quiz.html', question=questions) 
    #key = list(social_engs)
    questions_shuffled = shuffle(social_engs)#sample(key,3)
    for i in social_engs.keys():
        random.shuffle(social_engs[i]) 
        
    
    
    app.nquestions = len(social_engs)
    currentN = int(session["current_question"])
    return render_template('socials.html', q=questions_shuffled, o=social_engs, ntot=app.nquestions, num=currentN)


if __name__ == '__main__':
    app.run(debug=True)