from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

base = declarative_base()
engine = sa.create_engine('sqlite:///app/app.db')
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)

from app.models import Answer

base.metadata.create_all()
answers = Answer.query.order_by(Answer.httphash).all()
print(f"{len(answers)} answers in database.")
for answer in answers:
    print(answer.getAnswer())