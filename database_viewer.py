from app.models import Answer

answers = Answer.query.all()
print(f"{len(answers)} answers in database.")
for answer in answers:
    print(answer.getAnswer())