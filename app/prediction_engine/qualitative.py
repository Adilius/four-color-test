import matplotlib
matplotlib.use('Agg')   # Use matplotlib as backend renderer
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import math

answersheet = [
    {1: "red", 2: "green", 3: "yellow", 4: "blue"}, #1
    {1: "yellow", 2: "red", 3: "green", 4: "blue"}, #2
    {1: "blue", 2: "red", 3: "green", 4: "yellow"}, #3
    {1: "red", 2: "green", 3: "blue", 4: "yellow"}, #4
    {1: "yellow", 2: "blue", 3: "red", 4: "green"}, #5
    {1: "yellow", 2: "green", 3: "red", 4: "blue"}, #6
    {1: "yellow", 2: "green", 3: "blue", 4: "red"}, #7
    {1: "green", 2: "yellow", 3: "blue", 4: "red"}, #8
    {1: "red", 2: "green", 3: "yellow", 4: "blue"}, #9
    {1: "green", 2: "blue", 3: "red", 4: "yellow"}, #10
    {1: "yellow", 2: "green", 3: "blue", 4: "red"}  #11
]

# Returns dict count of each personality type  
def getCounter(choices):
    counter = { "green": 0, "blue": 0, "red": 0, "yellow": 0 }       # Counter for each type
    for count, choice in enumerate(choices):                        # Count each color type
        counter[answersheet[count].get(choice)] += 1
    return counter


# Returns predicted colour
def predict(choices):
    counter = getCounter(choices)

    intra_extra = -counter.get('green')-counter.get('blue')+counter.get('red')+counter.get('yellow')
    people_task = -counter.get('green')-counter.get('yellow')+counter.get('blue')+counter.get('red')

    if intra_extra < 0 and people_task < 0:
        return 'green'
    if intra_extra < 0 and people_task > 0:
        return 'blue'
    if intra_extra > 0 and people_task > 0:
        return 'red'
    if intra_extra > 0 and people_task < 0:
        return 'yellow'

    return 'NaN' # Incase for some reason 


# Returns procentage of each color depending on distance to each corner
def getColorProcentage(choices):

    questionsLength = len(choices)

    # Get x,y position of dot
    userPosition = getPosition(choices)
    x = userPosition[0]
    y = userPosition[1]

    # Calculate the eucledian distance to each corner
    # Range = [0,31], 0 closest, 31 furthest
    green_distance = math.sqrt(pow(x+questionsLength, 2) + pow(y+questionsLength, 2))
    blue_distance = math.sqrt(pow(x+questionsLength, 2) + pow(y-questionsLength, 2))
    red_distance = math.sqrt(pow(x-questionsLength, 2) + pow(y-questionsLength, 2))
    yellow_distance = math.sqrt(pow(x-questionsLength, 2) + pow(y+questionsLength, 2))

    # Calculate max value
    max_value = math.sqrt(pow(questionsLength*2, 2) + pow(questionsLength*2, 2))

    # Normalize distances to [0,1]
    green_distance_normalized = green_distance/max_value
    blue_distance_normalized = blue_distance/max_value
    red_distance_normalized = red_distance/max_value
    yellow_distance_normalized = yellow_distance/max_value
    
    #print(f'{max_value=}')
    #print(f'{green_distance=},{blue_distance=},{red_distance=},{yellow_distance=}')
    #print(f'{green_distance_normalized=},{blue_distance_normalized=},{red_distance_normalized=},{yellow_distance_normalized=}')

    # Inverse the distance to get procentage
    green_distance_inversed = 1-green_distance_normalized
    blue_distance_inversed = 1-blue_distance_normalized
    red_distance_inversed = 1-red_distance_normalized
    yellow_distance_inversed = 1-yellow_distance_normalized

    green_procentage = int(round((green_distance_inversed)*100))
    blue_procentage = int(round((blue_distance_inversed)*100))
    red_procentage = int(round((red_distance_inversed)*100))
    yellow_procentage = int(round((yellow_distance_inversed)*100))

    color_procentages = {
        'Green:': green_procentage,
        'Blue:': blue_procentage,
        'Red:': red_procentage,
        'Yellow:': yellow_procentage
    }

    color_procentages = dict(sorted(color_procentages.items(), key=lambda item: item[1], reverse=True))

    return color_procentages


# Returns x,y position of choices
def getPosition(choices):
    counter = getCounter(choices)

    x = -counter.get('green')-counter.get('blue')+counter.get('red')+counter.get('yellow')
    y = -counter.get('green')-counter.get('yellow')+counter.get('blue')+counter.get('red')

    return [x, y]