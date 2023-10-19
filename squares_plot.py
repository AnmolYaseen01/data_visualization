import matplotlib.pyplot as plt
x_values=range(1, 1001)
y_values=[x**2 for x in x_values]
plt.style.use('fivethirtyeight')
fig, ax=plt.subplots()
#The variable fig represents the entire figure or collection of plots that are generated.
'''The variable ax represents a single plot in the figure and is 
the variable we’ll use most of the time.'''
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues, s=10) # type: ignore
'''We pass the list of y-values to c, and then tell pyplot which colormap to 
use using the cmap argument. This code colors the points with lower y-values 
light blue and colors the points with higher y-values dark blue'''
ax.plot(x_values, y_values, linewidth=3)
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Root", fontsize=14)
ax.tick_params(axis="both", labelsize=14 )
#set the range for each axis
ax.axis=([0,1100,0,1100000 ])
plt.savefig('squares_plot.png', bbox_inches='tight')    #removes extra white spaces around the plot
plt.show()
