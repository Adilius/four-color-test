from app import db

class Answer(db.Model):
    __tablename__ = 'Answer'
    webhash = db.Column(db.String(32), nullable=False, primary_key=True)
    httphash = db.Column(db.String(32), nullable=False, primary_key=True)
    combinedhash = db.Column(db.String(32), nullable=False, primary_key=True)
    choices = db.Column(db.PickleType, nullable=False)

    def getAnswer(self):
        return [self.webhash, self.httphash, self.combinedhash, self.choices]

    def __repr__(self):
        #return [self.webhash, self.httphash, self.combinedhash, self.choices]
        return "<Answer(Webhash='%s', HTTPhash='%s', combinedhash='%s', Choices='%s')>'" % (self.webhash, self.httphash, self.combinedhash, self.choices)
