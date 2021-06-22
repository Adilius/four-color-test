from app import db

class Answer(db.Model):
    fingerprint = db.Column(db.String(64), nullable=False, primary_key=True)
    choices = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return "<Answer(Fingerprint='%s', Choices='%s')>'" % (self.fingerprint, self.choices)
