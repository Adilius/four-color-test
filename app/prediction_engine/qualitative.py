import matplotlib
matplotlib.use('Agg')   # Use matplotlib as backend renderer
import matplotlib.pyplot as plt
import io
import base64
import math

answersheet = [
    {1: "red", 2: "green", 3: "yellow", 4: "blue"}, #1
    {1: "yellow", 2: "blue", 3: "red", 4: "green"}, #2
    {1: "yellow", 2: "green", 3: "red", 4: "blue"}, #3
    {1: "yellow", 2: "red", 3: "green", 4: "blue"}, #4
    {1: "green", 2: "blue", 3: "red", 4: "yellow"}, #5
    {1: "green", 2: "yellow", 3: "blue", 4: "red"}, #6
    {1: "red", 2: "green", 3: "blue", 4: "yellow"}, #7
    {1: "yellow", 2: "green", 3: "blue", 4: "red"}, #8
    {1: "yellow", 2: "green", 3: "blue", 4: "red"}, #9
    {1: "red", 2: "green", 3: "yellow", 4: "blue"} #10
]

# Returns dict count of each personality type  
def getCounts(choices):
    counter = { "green": 0, "blue": 0, "red": 0, "yellow": 0 }       # Counter for each type
    for count, choice in enumerate(choices):       # Count each color type
        counter[answersheet[count].get(choice)] += 1
    return counter

# Returns base64 image plot of personality type plotted on graph
def createPlot(choices):
    counter = getCounts(choices)
    img = io.BytesIO()

    fig,ax = plt.subplots(figsize=(5,5))
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

    plt.xticks([])
    plt.yticks([])

    ax.axvline(0,color = 'black',linestyle='solid',linewidth=1)
    ax.axhline(0,color = 'black',linestyle='solid',linewidth=1)

    ax.fill_between([-10, 0],-10,0,alpha=0.9, color='#00FF00')  # green
    ax.fill_between([-10, 0], 0, 10, alpha=0.9, color='#0000FF')  # blue
    ax.fill_between([0, 10], 0, 10, alpha=0.9, color='#FF0000')  # red
    ax.fill_between([0, 10], -10, 0, alpha=0.9, color='#FFFF00')  # yellow

    x = -counter.get('green')-counter.get('blue')+counter.get('red')+counter.get('yellow')
    y = -counter.get('green')-counter.get('yellow')+counter.get('blue')+counter.get('red')
    plt.plot(x, y, marker='o', markersize=7, color='black')

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.savefig(img, format='png', bbox_inches='tight', pad_inches = 0, transparent=True)

    plot_img = base64.b64encode(img.getvalue()).decode()

    return plot_img

# Pie Chart helper function
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        if val == 0:
            return ''
        return '{v:d}'.format(v=val)
    return my_format

# Returns base64 image pie chart of selected choices
def createPieChart(choices):
    counter = getCounts(choices)
    values = list(counter.values())
    colors = ['#00FF00', '#0000FF', '#FF0000', '#FFFF00']
    labels = values
    img = io.BytesIO()
    fig, ax = plt.subplots(figsize=(5,5))
    patches, texts, autotexts = ax.pie(
        values, colors = colors, autopct = autopct_format(values),
        wedgeprops={'alpha':0.9},
        textprops={'size':'x-large'})
    plt.setp(autotexts, color='white', fontweight='bold')
    plt.tight_layout()
    ax.axis('equal')

    plt.plot()
    plt.savefig(img, format='png', bbox_inches='tight', pad_inches = 0, transparent=True)

    pie_img = base64.b64encode(img.getvalue()).decode()
    return pie_img

# Returns list of predicted personality types
def predict(choices):
    counter = getCounts(choices)

    intra_extra = -counter.get('green')-counter.get('blue')+counter.get('red')+counter.get('yellow')
    people_task = -counter.get('green')-counter.get('yellow')+counter.get('blue')+counter.get('red')

    colors = []

    if intra_extra < 0 and people_task < 0:
        colors.append('green')
    if intra_extra < 0 and people_task == 0:
        colors.append('green')
        colors.append('blue')
    if intra_extra < 0 and people_task > 0:
        colors.append('blue')
    if intra_extra == 0 and people_task > 0:
        colors.append('blue')
        colors.append('red')
    if intra_extra > 0 and people_task > 0:
        colors.append('red')
    if intra_extra > 0 and people_task == 0:
        colors.append('red')
        colors.append('yellow')
    if intra_extra > 0 and people_task < 0:
        colors.append('yellow')
    if intra_extra == 0 and people_task < 0:
        colors.append('yellow')
        colors.append('green')
    if intra_extra == 0 and people_task == 0:
        colors.append('yellow')
        colors.append('green')
        colors.append('blue')
        colors.append('red')

    return colors, counter

# Returns number instead of list of predicted personality type
def predictNumber(choices):
    colors, counter = predict(choices)

    if set(['green','yellow','blue','red']) == set(colors):
        prediction = 1

    elif set(['yellow','red']) == set(colors):
        prediction = 2

    elif set(['red']) == set(colors):
        prediction = 3

    elif set(['blue','red']) == set(colors):
        prediction = 4

    elif set(['blue']) == set(colors):
        prediction = 5

    elif set(['green','blue']) == set(colors):
        prediction = 6
        print('6')

    elif set(['green']) == set(colors):
        prediction = 7

    elif set(['green','yellow']) == set(colors):
        prediction = 8

    elif set(['yellow']) == set(colors):
        prediction = 9

    return prediction, counter

# Returns procentage of each color depending on distance to each corner
def getProcentage(choices):
    counter = getCounts(choices)

    x = -counter.get('green')-counter.get('blue')+counter.get('red')+counter.get('yellow')
    y = -counter.get('green')-counter.get('yellow')+counter.get('blue')+counter.get('red')

    green_distance = math.sqrt(pow(x+10, 2) + pow(y+10, 2))
    green_distance_inversed = 1/green_distance

    blue_distance = math.sqrt(pow(x+10, 2) + pow(y-10, 2))
    blue_distance_inversed = 1/blue_distance

    red_distance = math.sqrt(pow(x-10, 2) + pow(y-10, 2))
    red_distance_inversed = 1/red_distance

    yellow_distance = math.sqrt(pow(x-10, 2) + pow(y+10, 2))
    yellow_distance_inversed = 1/yellow_distance

    total = green_distance + blue_distance + red_distance + yellow_distance
    inversed_total = green_distance_inversed + blue_distance_inversed + red_distance_inversed + yellow_distance_inversed

    green_procentage = int(round((green_distance_inversed/inversed_total)*100))
    blue_procentage = int(round((blue_distance_inversed/inversed_total)*100))
    red_procentage = int(round((red_distance_inversed/inversed_total)*100))
    yellow_procentage = int(round((yellow_distance_inversed/inversed_total)*100))

    '''
    print("X:", x, " Y:", y)
    print("Green distance:", green_distance)
    print("Green inversed:", green_distance_inversed)
    print("Green procentage:", green_procentage)
    print("Blue distance:", blue_distance)
    print("Blue distance inversed:", blue_distance_inversed)
    print("Blue procentage:", blue_procentage)
    print("Red distance:", red_distance)
    print("Red distance inversed:", red_distance_inversed)
    print("Red procentage:", red_procentage)
    print("Yellow distance:", yellow_distance)
    print("Yellow distance inversed:", yellow_distance_inversed)
    print("Yellow procentage:", yellow_procentage)
    print("Total:", total)
    print("Inversed total:", inversed_total)
    '''

    return [green_procentage, blue_procentage, red_procentage, yellow_procentage]