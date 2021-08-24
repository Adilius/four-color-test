from flask import Flask, render_template, url_for, request, redirect, session
from app import app, db
from app.models import Answer
from app.prediction_engine import qualitative
from app.identifier_engine import fingerprint
from app.visualization_engine import plots


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':

        # Get user data
        choices = list(map(int, list(request.form.to_dict().values())[:-1]))
        web_hash = list(request.form.to_dict().values())[-1:][0]

        # Store data in session
        session['choices'] = choices
        session['web_hash'] = web_hash

        return redirect(url_for('result'))

    return render_template('quiz.html')


@app.route('/result')
def result():

    # Check if session has required data
    if not 'choices' in session or not 'web_hash' in session:
        return redirect(url_for('index'))

    # Get data from session
    user_choices = session['choices']
    web_hash = session['web_hash']

    # Compute combined hash
    user_combined_hash = fingerprint.create_fingerprint(request, web_hash)

    # Predict color
    user_color = qualitative.predict(user_choices)

    # Compute color counts
    user_color_counter = qualitative.getCounter(user_choices)

    # Compute color procentages
    user_color_procentages = qualitative.getColorProcentage(user_choices)

    # Compute user x,y position
    user_position = qualitative.getPosition(user_choices)

    # Create color plot
    plot_url = plots.createPlot(user_position)

    # Create all user plot
    answers = db.session.query(Answer.result)
    user_x_position_list = []
    user_y_position_list = []
    for answer in answers:
        user_x_position_list.append(answer[0][0])
        user_y_position_list.append(answer[0][1])
    
    # Create plot base64
    all_plot_url = plots.plotAll(user_x_position_list, user_y_position_list)


    # If we are in development config 
    if app.config['ENV'] == 'Development':
        print('---- User entry ----')
        print(f'Combined hash: {user_combined_hash}')
        print(f'Counter: {user_color_counter}')
        print(f'Color procentages: {user_color_procentages}')
        print(f'User position: {user_position}')
        print(f'User color: {user_color}')

    # Create an answer to push to database
    answer = Answer(combined_hash = user_combined_hash,
                    choices = user_choices,
                    counters = user_color_counter,
                    color_procentages = user_color_procentages,
                    result = user_position,
                    color = user_color)

    # Add to database
    try:
        db.session.merge(answer)
        db.session.commit()
        print(f'Pushed answer to database: {user_combined_hash}')
    except:
        print("Error pushing to database.")

    # Render result webpage
    return render_template('result.html',
                           prediction=user_color,
                           plot_url=plot_url,
                           all_plot_url = all_plot_url,
                           user_color_procentages=user_color_procentages)


@app.route('/personalities')
def personalities():
    return render_template('personalities.html')

# Handle 404 errors
@app.errorhandler(404)
def error_404(error):
    print(error)
    return render_template('404.html'), 404
