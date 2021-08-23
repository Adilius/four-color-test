from app import db

class Answer(db.Model):
    __tablename__ = 'Answer'
    combined_hash = db.Column(db.String(32), nullable=False, primary_key=True)  # Unique hash
    choices = db.Column(db.PickleType, nullable=False)                          # User choices
    counters = db.Column(db.PickleType, nullable=False)                         # Counter of those choices
    color_procentages = db.Column(db.PickleType, nullable=False)                # Procentage of each color
    result = db.Column(db.PickleType, nullable=False)                           # Predicted color
    color = db.Column(db.Integer, nullable=False)

    # Returns answer in list
    def getAnswer(self):
        return [self.combined_hash, self.choices, self.counters, self.color_procentages, self.result, self.color]

    def __repr__(self):
        return (f'<Answer({self.combined_hash=}, {self.choices=}, {self.counters=}, {self.color_procentages=}, {self.result=}, {self.color=}>')