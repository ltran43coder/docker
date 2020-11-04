# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [0,0.5,1,2,3,4,5,6,7,8,9,9.5,10,9,8,7,6,5,4,3,2,1,0.5,0]
# corresponding y axis values
y = [5,6,6.5,7,6.5,6,5,6,6.5,7,6.5,6,6,3.5,2,1,0.5,0,0.5,1,2,3.5,4.5,5]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()