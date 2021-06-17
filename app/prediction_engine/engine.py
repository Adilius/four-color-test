import enum

answersheet = [
    {"1": "green", "2": "blue", "3": "red", "4": "yellow"},
    {"1": "green", "2": "blue", "3": "red", "4": "yellow"},
    {"1": "green", "2": "blue", "3": "red", "4": "yellow"}
]

class prediction():

    def __init__(self, choices):
        self.choices = choices
        self.counter = {
        "green": 0, "blue": 0, "red": 0, "yellow": 0        # Counter for each type
    }

    '''
    Needs to correspond to question asked in quiz.html
    '''
    def predict(self):
        for count, choice in enumerate(self.choices):
            print("Count:",count, "  choice:",choice)
            print("Answersheet:", answersheet[count].get(choice))
            self.counter[answersheet[count].get(choice)] += 1
        print(self.counter)
        
