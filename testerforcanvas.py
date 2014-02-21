from Tkinter import Tk, Canvas, Frame, PhotoImage, Entry
import math

##DO NOT EDIT ANY MANUALLY INPUTTED CONSTRUCTOR NUMBER VALUES


##FOR BOTH ATOMIC AND QWERTY SETUP

root = Tk()

isQwerty = False #sets whether or not to use a qwerty keyboard
fcW = 480 #Frame and Canvas X
fcH = 200 #Frame and Canvas Y
cciX = 0 # Canvas Create Image X
cciY = 0 # Canvas Create Image Y
root.geometry("480x250+400+300")

if isQwerty:
    cciX = 239
    cciY = 95
    photo = PhotoImage(file="qwerty.gif")
else:
    cciX = 243
    cciY = 113
    photo = PhotoImage(file="atomic.gif")

root.update() #update our root with new dimensions

lines = [] # for appending to lineNumber
lineNumber = []  # keeps track of line item numbers to delete later
toSum = [] # (oldpoint.x, oldpoint.y), (newpoint.x, newpoint.y), dist(previous tuples listed))

frame = Frame(root, width = fcW, height = fcH) #create a frame in root
frame.pack() #put it in the window

canvas = Canvas(frame, width = fcW, height = fcH) #create a canvas
canvas.create_image(cciX, cciY, image = photo) #put a image in the canvas
canvas.pack() #put it in the frame

result = Entry(root, font = ("Times", 14)) #create a results box
result.pack() #put it in the window

def dist(oldCoord, newCoord):
    return math.sqrt(math.pow((newCoord[0]-oldCoord[0]), 2)+math.pow((newCoord[1]-oldCoord[1]), 2))

def getReturn(toSum):
    length = 0
    for i in range(len(toSum)):
        length += toSum[i][2]
    return length

def callback(event, reset): #note, when sending to database, add 400 to x and 300 to y
    global lines
    global lineNumber
    global toSum
    global canvas
    if reset == 1: #if we release the button
        for i in range(len(lineNumber)): #delete the lines drawn
            canvas.delete(lineNumber[i])
        if len(lines) > 1: # if it was dragged
            value = ((400+lines[0][0], 300+lines[0][1]), (400+lines[-1][0], 300+lines[-1][1]), getReturn(toSum))
        else: #if it was clicked
            value = ((400+event.x, 300+event.y), (0,0), 0)
        lineNumber = [] #empty our lists
        lines = []
        toSum = []
        print(value) #return the start, end and distance travelled
        return
    if (len(lines)) == 0: #if we just started drawing
        lines.append((event.x, event.y))
    else: #we're in the middle of drawing
        toSum.append(((lines[-1][0], lines[-1][1]), (event.x, event.y), dist((lines[-1][0], lines[-1][1]), (event.x, event.y))))
        lineNumber.append(canvas.create_line((lines[-1][0], lines[-1][1]), (event.x, event.y), fill="red"))
        lines.append((event.x, event.y))

canvas.bind("<B1-Motion>",func = lambda event: callback(event, 0), add = "+")
canvas.bind("<ButtonRelease-1>", func = lambda event: callback(event, 1))

root.mainloop()
