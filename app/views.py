from flask import Flask, render_template, url_for, request, redirect, session
from app import app, db
from app.models import Answer
from app.prediction_engine import qualitative
from app.identifier_engine import fingerprint

import random

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        choices = list(map(int, list(request.form.to_dict().values())[:-1]))
        web_fingerprint = list(request.form.to_dict().values())[-1:][0]
        user_fingerprint = fingerprint.create_fingerprint(request, web_fingerprint)
        print(choices)
        session['choices'] = choices
        session['user_fingerprint'] = user_fingerprint
        answer = Answer(fingerprint=user_fingerprint, choices=choices)

        try:
            db.session.merge(answer)
            db.session.commit()
            return redirect(url_for('result'))
        except:
            print("Error pushing to database.")
        
        return redirect(url_for('result'))
    
    return render_template('quiz.html')

@app.route('/result')
def result():
    current_choices = session['choices']
    user_fingerprint = session['user_fingerprint']
    prediction, counters = qualitative.predict(current_choices)
    plot_url = qualitative.createPlot(current_choices)
    answers = Answer.query.order_by(Answer.fingerprint).all()
    return render_template('result.html', prediction=prediction, counters=counters, user_fingerprint=user_fingerprint, answers=answers, plot_url=plot_url)

@app.errorhandler(404)
def error_404(error):
    print(error)
    return render_template('404.html'), 404