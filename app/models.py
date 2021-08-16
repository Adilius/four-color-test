from app import db

class Answer(db.Model):
    __tablename__ = 'Answer'
    combined_hash = db.Column(db.String(32), nullable=False, primary_key=True)
    choices = db.Column(db.PickleType, nullable=False)
    result = db.Column(db.PickleType, nullable=False)
    color = db.Column(db.Integer, nullable=False)

    # Returns answer in list
    def getAnswer(self):
        return [self.combined_hash, self.choices, self.result, self.color]

    def __repr__(self):
        return (f'<Answer({self.combined_hash=}, {self.choices=}, {self.result=}, {self.color=}>')