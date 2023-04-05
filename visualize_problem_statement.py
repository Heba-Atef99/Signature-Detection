import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np

def visualize_data(file_num=1, data_type='Train'):
    ROOT = "data/"

    fig = plt.figure()
    # # add axes to the image
    ax = fig.add_axes([0, 0, 1, 1])
    # # read and plot the image
    image_path = ROOT + data_type + 'Images/' + str(file_num) + '.tif'
    image = plt.imread(image_path)
    plt.imshow(image)

    file_path = ROOT + data_type + 'GroundTruth/' + str(file_num) + '.txt'

    with open(file_path, 'r') as f:
        line = f.readline()
        xmin, ymin, xmax, ymax = line.strip().split(',')
        xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

    width = xmax - xmin
    height = ymax - ymin

    # add bounding boxes to the image
    rect = patches.Rectangle((xmin, ymin), width, height, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    # plt.waitforbuttonpress(0)

visualize_data()