from app.models import Answer
import pandas as pd

answers = Answer.query.all()
print(f"{len(answers)} answers in database.")
for answer in answers[:20]:
    print(answer.getAnswer())