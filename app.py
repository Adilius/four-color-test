from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    answer_ip = db.Column(db.String(15), nullable=False)
    answer_choices = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return "<Answer(Id='%s', Ip='%s', Choices='%s')>'" % (self.answer_id, self.answer_ip, self.answer_choices)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answer_ip = request.remote_addr
        answer_choices = list(request.form.to_dict().values())
        print(answer_ip)
        print(answer_choices)
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
    answers = Answer.query.order_by(Answer.answer_id).all()
    return render_template('result.html', answers=answers)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)