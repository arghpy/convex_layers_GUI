# Import the required libraries
from tkinter import *
from tkinter import ttk



# Function to display the point and add it to listPoints
def draw_line(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y
    listPoints.append(Point(x1, y1))
    # Draw an oval in the given co-ordinates
    canvas.create_oval(x1,y1,x2,y2,fill="black", width=5)



# Finding the leftmost index
def Left_index(listPoints):
    minn = 0
    for i in range(1,len(listPoints)):
        if listPoints[i].x < listPoints[minn].x:
            minn = i
        elif listPoints[i].x == listPoints[minn].x:
            if listPoints[i].y > listPoints[minn].y:
                minn = i
    return minn



# Getting the orientation
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
        (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2



# Computing the Convex Hull of points
def convexHull_2(listPoints, n):
    
    # There must be at least 3 points
    if n < 3:
        return

    # Find the leftmost point
    l = Left_index(listPoints)

    hull = []
    
    p = l
    q = 0
    while(True):
        
        # Add current point to result
        hull.append(p)

        q = (p + 1) % n

        for i in range(n):
            if(orientation(listPoints[p],
                        listPoints[i], listPoints[q]) == 2):
                q = i

        p = q

        if(p == l):
            break

    # Create the lines
    holder_listPoints = []
    holder_listPoints = listPoints.copy()

    for index in range(len(hull)):
        if index != (len(hull) - 1): 
            canvas.create_line(listPoints[hull[index]].x, listPoints[hull[index]].y,\
            listPoints[hull[index + 1]].x, listPoints[hull[index + 1]].y)
            holder_listPoints.remove(listPoints[hull[index]])
        else:
            canvas.create_line(listPoints[hull[index]].x, listPoints[hull[index]].y,\
            listPoints[hull[0]].x, listPoints[hull[0]].y)
            holder_listPoints.remove(listPoints[hull[index]])

    listPoints = holder_listPoints.copy()
    convexHull_2(listPoints, len(listPoints))




# Delete all drawing from canvas and reset points list
def clearCanvas():
    canvas.delete("all")
    listPoints.clear()



# Point class with x, y as point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Create an instance of tkinter frame or window
win=Tk()
win.title("Convex Layers")


# Create a list to hold the points drawn by the user
listPoints = []


# Create a canvas widget
canvas=Canvas(win, width=700, height=500, background="white")
canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', draw_line)
click_num=0


# Add button to compute convex layers
button1 = Button(win, text = 'Compute Convex Layers', command = lambda: convexHull_2(listPoints, len(listPoints)))
button1.grid(row=1, column=0)

# Add button to reset canvas
button2 = Button(win, text = 'Reset', command = clearCanvas)
button2.grid(row=2, column=0)

win.mainloop()


