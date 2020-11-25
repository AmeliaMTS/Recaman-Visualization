import matplotlib.pyplot as plt
import numpy as np
import math

def pal(point, angle, length): #this plots a line starting at (point), with
    # unpack the first point    #certain angle and length
    x, y = point

    # find the end point
    endy = y + length * math.sin(math.radians(angle)) #calculates change in y and adds to starting value
    endx = x + length * math.cos(math.radians(angle)) #calculates change in x and adds to starting value

    # plots the line with the starting coordinate and the calculated end coordinate
    ax.plot([x, endx], [y,endy])

# end of plot function code

#this is where the elements of the recaman sequence get calculated and added to an array
recaman = []
crn = 0
elements = 1000

for i in range(1, elements):
    recaman.append(crn)
    if (crn - i in recaman) or (crn - i < 0):
        crn = crn + i
    else:
        crn = crn - i
#end of recaman calculation

x = 0
y = 0
angle = 0
length = 0
poly=3

fig, ax = plt.subplots() #creating figure
for i in range(1, elements):
    length = recaman[i-1]   #obtain length of next line
    pal((x, y), angle, length)  #((starting coordinate),
                                # angle of line relative to x-axis, length of line)
    y = y + length * math.sin(math.radians(angle)) #moves the new starting point to the old end point
    x = x + length * math.cos(math.radians(angle))

    if angle == 360-(180-((poly-2)*180)/poly): #resets angle to 0 to complete one full rotation
        angle = 0
    else:
        angle = angle + (180-((poly-2)*180)/poly) #adds 90 to angle to draw perpendicular line

plt.axis('scaled')
plt.show()
