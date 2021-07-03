from flask import Flask, render_template, url_for, request, redirect, session
from app import app, db
from app.models import Answer
from app.prediction_engine import qualitative
from app.identifier_engine import fingerprint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        choices = list(map(int, list(request.form.to_dict().values())[:-1]))
        web_fingerprint = list(request.form.to_dict().values())[-1:][0]
        webhash, httphash, combinedhash = fingerprint.create_fingerprint(request, web_fingerprint)
        session['choices'] = choices
        session['user_hases'] = webhash, httphash, combinedhash
        answer = Answer(webhash=webhash, httphash=httphash, combinedhash=combinedhash, choices=choices)

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
    webhash, httphash, combinedhash = session['user_hases']
    prediction, counters = qualitative.predictNumber(current_choices)
    plot_url = qualitative.createPlot(current_choices)
    answers = Answer.query.order_by(Answer.webhash).all()
    procentages = qualitative.getProcentage(current_choices)
    return render_template('result.html', prediction=prediction, counters=counters, user_fingerprint=[webhash, httphash, combinedhash], answers=answers, plot_url=plot_url, procentages=procentages)

@app.route('/personalities')
def personalities():
    return render_template('personalities.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def error_404(error):
    print(error)
    return render_template('404.html'), 404