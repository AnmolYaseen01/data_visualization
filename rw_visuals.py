import matplotlib.pyplot as plt
from random_walk import RandomWalk
'''make a random walk'''
while True:
    rw=RandomWalk()
    rw.fill_walk()
    # plot the points in the walk
    plt.style.use("classic")
    '''you can pass a figsize argument to set the size of the figure. The figsize parameter takes a tuple, which tells Matplotlib the dimensions of the plotting window in inches.Matplotlib assumes that your screen resolution is 100 pixels per inch; '''
    '''if you know your system’s resolution, pass plt.subplots() the resolution using the dpi parameter to set a plot size that makes effective use of the space available on your screen'''
    fig, ax=plt.subplots(figsize=(10,6), dpi=128)
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors="none",s=1) # type: ignore
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],c="red", edgecolors='none',s=100)
    #remove the axises
    ax.get_xaxis().set_visible=(False)
    ax.get_yaxis().set_visible=(False)
    plt.show()

    keep_running=input("make another walk?(y/n):")
    if keep_running=="n":
        break