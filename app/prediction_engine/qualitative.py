answersheet = [
    {"1": "red", "2": "green", "3": "yellow", "4": "blue"}, #1
    {"1": "yellow", "2": "blue", "3": "red", "4": "green"}, #2
    {"1": "yellow", "2": "green", "3": "red", "4": "blue"}, #3
    {"1": "yellow", "2": "red", "3": "green", "4": "blue"}, #4
    {"1": "green", "2": "blue", "3": "red", "4": "yellow"}, #5
    {"1": "green", "2": "yellow", "3": "blue", "4": "red"}, #6
    {"1": "red", "2": "green", "3": "blue", "4": "yellow"}, #7
    {"1": "yellow", "2": "green", "3": "blue", "4": "red"}, #8
    {"1": "yellow", "2": "green", "3": "blue", "4": "red"}, #9
    {"1": "red", "2": "green", "3": "yellow", "4": "blue"} #10
]

def predict(choices):
    counter = { "green": 0, "blue": 0, "red": 0, "yellow": 0 }       # Counter for each type
    for count, choice in enumerate(choices):       # Count each color type
        counter[answersheet[count].get(choice)] += 1

    highest_counts = max(counter.values())
    highest_counters = [k for k,v in counter.items() if v == highest_counts]

    return highest_counters, counter