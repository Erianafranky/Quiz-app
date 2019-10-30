import csv
import os
import random

from flask import Flask, flash, render_template, request, session

import questions as qm
from questions import *

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/phishing", methods=["GET", "POST"])
def phishing():
    with open("TemplateQuiz.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        quiz = list(reader)
        random.shuffle(quiz)
    if request.method == "POST":
        questions_file = "TemplateQuiz.csv"
        question = quiz[current_question_index][0]
        options = quiz[current_question_index][1:-1]
        correct_answer = quiz[current_question_index][-1]
        entered_answer = request.form.get("answer_phishing")
        if not entered_answer:
            flash("Please choose an answer", "error")
        else:
            curr_answer = request.form["answer_phishing"]
            correct_answer = quiz[current_question_index][-1]
        if curr_answer == correct_answer[: len(curr_answer)]:
            questions["wrong"].append(int(current_question_index))
        else:
            questions["wrong"].append(int(current_question_index))

        session[current_question_index] = str(current_question_index + 1)
        questions["curretq"] = max(int(session[current_question_index]), questions["curretq"])

    import pdb; pdb.set_trace()
    if current_question_index not in session:
        session[current_question_index] = 1

    elif int(session[current_question_index]) not in range(1, len(quiz)):
        questions["wrong"] = list(set(questions["wrong"]))
        questions["correct"] = list(set(questions["correct"]))
        return render_template("end-quiz.html", question=questions)


    currentN = int(session[current_question_index])
    currentQ = quiz[current_question_index][0]
    a1, a2, a3, a4 = quiz[current_question_index][1:-3]  # [1:-3] because you have 4 choices for now
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
