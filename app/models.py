from app import db

class Answer(db.Model):
    webhash = db.Column(db.String(32), nullable=False, primary_key=True)
    httphash = db.Column(db.String(32), nullable=False, primary_key=True)
    combinedhash = db.Column(db.String(32), nullable=False, primary_key=True)
    choices = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return "<Answer(Webhash='%s', HTTPhash='%s', combinedhash='%s', Choices='%s')>'" % (self.webhash, self.httphash, self.combinedhash, self.choices)
