import matplotlib
matplotlib.use('Agg')   # Use matplotlib as backend renderer
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import kde
import io
import base64

# Returns base64 image plot of personality type plotted on graph
def createPlot(user_position):
    img = io.BytesIO()

    x_left_limit = -11.5
    x_right_limit = 11.5

    y_upper_limit = 11.5
    y_lower_limit = -11.5

    fig,ax = plt.subplots(figsize=(5,5))
    ax.set_xlim(x_left_limit,x_right_limit)
    ax.set_ylim(y_lower_limit,y_upper_limit)

    plt.xticks([])
    plt.yticks([])

    ax.axvline(0,color = 'black',linestyle='solid',linewidth=1)
    ax.axhline(0,color = 'black',linestyle='solid',linewidth=1)

    # [x1, x2], y1, y2
    ax.fill_between([x_left_limit, 0], y_lower_limit,0,alpha=0.9, color='#00FF00')  # Green
    ax.fill_between([x_left_limit, 0], 0, y_upper_limit, alpha=0.9, color='#0000FF')  # blue
    ax.fill_between([0, x_right_limit], 0, y_upper_limit, alpha=0.9, color='#FF0000')  # red
    ax.fill_between([0, x_right_limit], y_lower_limit, 0, alpha=0.9, color='#FFFF00')  # yellow

    x = user_position[0]
    y = user_position[1]
    plt.plot(x, y, marker='o', markersize=7, color='black')

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.savefig(img, format='png', bbox_inches='tight', pad_inches = 0, transparent=True)

    plot_img = base64.b64encode(img.getvalue()).decode()

    return plot_img


def plotAll(x, y):
    img = io.BytesIO()

    fig,ax = plt.subplots(figsize=(5,5))
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

    plt.xticks([])
    plt.yticks([])

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.savefig(img, format='png', bbox_inches='tight', pad_inches = 0, transparent=True)

    plot_img = base64.b64encode(img.getvalue()).decode()

    return plot_img