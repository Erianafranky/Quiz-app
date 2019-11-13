import csv
import os
import random
import questions as qm
from flask import Flask, flash, redirect, url_for, render_template, request, session

from flask import Flask, flash, render_template, request, session

import questions as qm
from questions import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

with open("TemplateQuiz.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        quiz = list(reader)
        random.shuffle(quiz)

@app.route("/phishing", methods=["GET", "POST"])
def phishing():
    if request.method == "POST":
        correct_answer = quiz[questions["currentq"]-1][-1]
        entered_answer = request.form.get("answer_phishing")
        if not entered_answer:
            flash("Please choose an answer", "error")
        else:
            if entered_answer == correct_answer:
                questions["correct"].append(int(questions["currentq"]))
            else:
                questions["wrong"].append(int(questions["currentq"]))

        # (session[current_question_index]) = str(current_question_index + 1)
        # questions["currentq"] = max(int(session[current_question_index]), questions["currentq"])
        questions["currentq"] += 1
        print(questions)
        # if int(session[current_question_index]) in quiz:
        if questions["currentq"] in range(1, len(quiz) + 1):
            # import pdb; pdb.set_trace()
            # current_question_index += 1
            session[str(questions["currentq"])] = questions["currentq"]
            redirect(url_for('phishing'))
        else:
            questions["wrong"] = list(set(questions["wrong"]))
            questions["correct"] = list(set(questions["correct"]))
            return render_template('end-quiz.html', question=questions)

    # import pdb; pdb.set_trace()
    if not session:
        session[str(questions["currentq"])] = 1

    # elif int(session[current_question_index]) not in quiz:
    elif questions["currentq"] not in range(1, len(quiz) + 1):
        questions["currentq"] = 1
        questions["wrong"], questions["correct"] = [], []
        redirect(url_for('phishing'))

    currentN = int(session[str(questions["currentq"])])
    currentQ = quiz[currentN - 1][0]
    a1, a2, a3, a4 = quiz[currentN - 1][1:-3]  # [1:-3] because you have 4 choices for now
    app.nquestions = len(quiz)
    return render_template(
        "socials.html",
        num=currentN,
        ntot=app.nquestions,
        question=currentQ,
        ans1=a1,
        ans2=a2,
        ans3=a3,
        ans4=a4,
    )


if __name__ == "__main__":
    app.run(debug=True)
