import sys
import random, os, binascii
from app import db
from app.models import Answer
from app.prediction_engine import qualitative

def generateAnswer():

    # Generate random data
    combined_hash = binascii.b2a_hex(os.urandom(16)).decode('utf-8')
    choices = [random.randrange(1, 5, 1) for _ in range(10)]

    # Compute using random data
    user_color, _ = qualitative.predictNumber(choices)
    user_position = qualitative.getPosition(choices)

    # Create an answer to push to database
    answer = Answer(combined_hash = combined_hash,
                    choices = choices,
                    result = user_position,
                    color = user_color)

    # Push to database
    try:
        db.session.merge(answer)
        db.session.commit()
        print(f'Pushed answer to database: {combined_hash}')
    except:
        print("Error pushing to database.")

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print(f'Wrong argument length')
        sys.exit(1)
    
    x = sys.argv[1]
    if not x.isdigit():
        print(f'Wrong input type')
        sys.exit(1)
    
    for _ in range(int(x)):
        generateAnswer()
    