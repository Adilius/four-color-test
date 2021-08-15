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

        # Get user data
        choices = list(map(int, list(request.form.to_dict().values())[:-1]))
        web_fingerprint = list(request.form.to_dict().values())[-1:][0]

        # Compute combined hash
        combined_hash = fingerprint.create_fingerprint(request, web_fingerprint)

        # Store data in session
        session['choices'] = choices
        session['user_hash'] = combined_hash

        return redirect(url_for('result'))

    return render_template('quiz.html')


@app.route('/result')
def result():

    # Check if session has required data
    if not 'choices' in session or not 'user_hash' in session:
        return redirect(url_for('index'))

    # Get data from session
    choices = session['choices']
    combined_hash = session['user_hash']

    # Predict color, and return color counters
    user_color, counters = qualitative.predictNumber(choices)

    # Create color plot
    plot_url = qualitative.createPlot(choices)

    # Compute color procentages
    color_procentages = qualitative.getColorProcentage(choices)

    # Compute user x,y position
    user_position = qualitative.getPosition(choices)


    # If we are in development config 
    if app.config['ENV'] == 'Development':
        answers = Answer.query.order_by(Answer.combined_hash).all()

    # Create an answer to push to database
    answer = Answer(combined_hash = combined_hash,
                    choices = choices,
                    result = user_position,
                    color = user_color)

    try:
        db.session.merge(answer)
        db.session.commit()
        print(f'Pushed answer to database: {combined_hash}')
    except:
        print("Error pushing to database.")

    return render_template('result.html',
                           prediction=user_color,
                           counters=counters,
                           user_fingerprint=combined_hash,
                           plot_url=plot_url,
                           color_procentages=color_procentages)


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
