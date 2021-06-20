from flask import Flask, render_template, url_for, request, redirect, session
from app import app, db
from app.models import Answer
from app.prediction_engine import qualitative

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answer_ip = request.remote_addr
        answer_choices = list(request.form.to_dict().values())
        session['answer_choices'] = answer_choices
        new_answer = Answer(answer_ip=answer_ip, answer_choices=answer_choices)

        try:
            db.session.add(new_answer)
            db.session.commit()
            return redirect(url_for('result'))
        except:
            print("Error pushing to database.")
        
        return redirect(url_for('result'))
    
    return render_template('quiz.html')

@app.route('/result')
def result():
    current_choices = session['answer_choices']
    prediction, counters = qualitative.predict(current_choices)
    answers = Answer.query.order_by(Answer.answer_id).all()
    return render_template('result.html', prediction=prediction, counters=counters, answers=answers)

@app.errorhandler(404)
def error_404(error):
    print(error)
    return render_template('404.html'), 404