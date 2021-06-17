from app import db

class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    answer_ip = db.Column(db.String(15), nullable=False)
    answer_choices = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return "<Answer(Id='%s', Ip='%s', Choices='%s')>'" % (self.answer_id, self.answer_ip, self.answer_choices)
