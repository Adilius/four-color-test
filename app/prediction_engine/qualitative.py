import matplotlib.pyplot as plt
import io
import base64

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

# Returns count of each personality type  
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

    ax.fill_between([-10, 0],-10,0,alpha=0.3, color='#00FF00')  # green
    ax.fill_between([0, 10], -10, 0, alpha=0.3, color='#FFFF00')  # yellow
    ax.fill_between([-10, 0], 0, 10, alpha=0.3, color='#0000FF')  # blue
    ax.fill_between([0, 10], 0, 10, alpha=0.3, color='#FF0000')  # red

    x = -counter.get('green')-counter.get('blue')+counter.get('red')+counter.get('yellow')
    y = -counter.get('green')-counter.get('yellow')+counter.get('blue')+counter.get('red')
    plt.plot(x, y, marker='o', markersize=5, color='black')

    plt.plot()
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.savefig(img, format='png', bbox_inches='tight', pad_inches = 0)

    plot_img = base64.b64encode(img.getvalue()).decode()
    return plot_img

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
        print("1")

    elif set(['yellow','red']) == set(colors):
        prediction = 2
        print('2')

    elif set(['red']) == set(colors):
        prediction = 3
        print('3')

    elif set(['blue','red']) == set(colors):
        prediction = 4
        print('4')

    elif set(['blue']) == set(colors):
        prediction = 5
        print('5')

    elif set(['green','blue']) == set(colors):
        prediction = 6
        print('6')

    elif set(['green']) == set(colors):
        prediction = 7
        print('7')

    elif set(['green','yellow']) == set(colors):
        prediction = 8
        print('8')

    elif set(['yellow']) == set(colors):
        prediction = 9
        print('9')

    return prediction, counter