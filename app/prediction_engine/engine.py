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
        for count, choice in enumerate(self.choices):       # Count each color type
            self.counter[answersheet[count].get(choice)] += 1
        print(self.counter)

    def predict(self):
        highest_counts = max(self.counter.values())
        highest_counters = [k for k,v in self.counter.items() if v == highest_counts]

        print(highest_counters)
        pass
        
        
