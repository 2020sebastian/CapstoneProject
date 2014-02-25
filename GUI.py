from Tkinter import Tk, Canvas, Frame, PhotoImage, Entry, Label, Button, END
import math, csv, os
from sqlite3 import *

noMechFlag = False
noPILFlag = False
#from PIL import Image, ImageTk

try:
    import mechanize
except ImportError:
    noMechFlag = True
    print("Sorry, you need Mechanize for Python 2.7 installed")
    print("First, download SetupTools at :\nhttp://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe#md5=57e1e64f6b7c7f1d2eddfc9746bbaf20")
    print("Then, in the command prompt, type : easy_install mechanize")

try:
    from PIL import Image, ImageTk
except ImportError:
    noPILFlag = True
    print("\nSorry, you need PIL for Python 2.7 installed")
    print("First, download PIL-1.1.7.win32-py2.7 at :\nhttp://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe")
    print("Then run the executable")


if noMechFlag or noPILFlag:
    exit


#words for testing
#cat
#cut
#dairy
#daira
#daiva
#daitya

##DO NOT EDIT ANY MANUALLY INPUTTED CONSTRUCTOR NUMBER VALUES

#DEVMODE VARIABLES BELOW
isDev = False       # activates our devMode function
devKeyContainer = [('q',(30,30)), ('w',(85,30)), ('e',(141,30)), ('r',(195,30)), ('t',(251,30)), ('y',(306,30)), ('u',(361,30)), ('i',(417,30)), ('o',(472,30)), ('p',(528,30)),
              ('resetL1',(30,82)), ('a',(85,82)), ('s',(141,82)), ('d',(195,82)), ('f',(251,82)), ('g',(306,82)), ('h',(361,82)), ('j',(417,82)), ('k',(472,82)), ('l',(528,82)),
              ('resetL2',(30,136)), ('z',(85,136)), ('x',(141,136)), ('c',(195,136)), ('v',(251,136)), ('b',(306,136)), ('n',(361,136)), ('m',(417,136)), ('resetR1',(472,136)), ('resetR2',(528,136))]
if isDev:
    devKeyLength = 24   #used for our devMode function to draw lines and put coordinates into a csv file
    devCoordListContainer = []
    devCurrentKey = ''
    devKeyCounter = 0 #placer for array devKeyContainer
    devLineIDContainer = []
#END DEVMODE VARIABLES

def devMode(x,y):
##    Written by Joe (code ninja) Banass
##    This function may become deprecated. Its main 
##    function was to help create our input data for  
##    generating the sokograph coordinate data. Trigger 
##    its use with changing the global variable isDev
##    to True
    global devCurrentKey, devKeyContainer, devCoordListContainer, devKeyCounter
    devCurrentKey = devKeyContainer[devKeyCounter][0] # we assign the next key to the variable to write to
    devKeyCounter += 1
    for i in range(5): #think of below as a unit circle
        if i == 0:
            devCoordListContainer.append((x,y))
        if i == 1:
            devCoordListContainer.append((x-devKeyLength,y-devKeyLength))
            devLineIDContainer.append(canvas.create_line(x,y,x-devKeyLength,y-devKeyLength))
        if i == 2:
            devCoordListContainer.append((x+devKeyLength, y-devKeyLength))
            devLineIDContainer.append(canvas.create_line(x-devKeyLength,y-devKeyLength,x+devKeyLength,y-devKeyLength))
        if i == 3:
            devCoordListContainer.append((x-devKeyLength, y+devKeyLength))
            devLineIDContainer.append(canvas.create_line(x+devKeyLength,y-devKeyLength,x-devKeyLength,y+devKeyLength))
        if i == 4:
            devCoordListContainer.append((x+devKeyLength, y+devKeyLength))
            devLineIDContainer.append(canvas.create_line(x-devKeyLength,y+devKeyLength,x+devKeyLength,y+devKeyLength))
            devLineIDContainer.append(canvas.create_line(x+devKeyLength,y+devKeyLength,x-devKeyLength,y-devKeyLength))

    print("writing {} with coords {}").format(devKeyContainer[devKeyCounter-1],devCoordListContainer)
    writer = csv.writer(open('coords.csv','ab'), delimiter=',')                
    writer.writerow([devCurrentKey] +
                    [devCoordListContainer[0][0]] +
                    [devCoordListContainer[0][1]] +
                    [devCoordListContainer[1][0]] +
                    [devCoordListContainer[1][1]] +
                    [devCoordListContainer[2][0]] +
                    [devCoordListContainer[2][1]] +
                    [devCoordListContainer[3][0]] +
                    [devCoordListContainer[3][1]] +
                    [devCoordListContainer[4][0]] +
                    [devCoordListContainer[4][1]])
    devCoordListContainer = [] #we empty the coordinate list for new key coordinates

#added by joe
def search(x1, y1, x2, y2, length, email, CBUserIntervalIDContainer):
    br.open("http://joelguth.com:8000/test/test2.php")
    br.select_form(nr=0)
    br.form['startx'] = str(x1)
    br.form['starty'] = str(y1)
    br.form['endx'] = str(x2)
    br.form['endy'] = str(y2)
    br.form['length'] = str(length)
    br.submit()

    result = br.response().read()
    result = result.split("<br />")

    result = result[2:]

    for i in range(len(result)):
        result[i] = result[i][0:result[i].find(",")]

    totalItems = len(result)

    toReturn = []

    for i in range(totalItems):
        if i == totalItems or i == totalItems - 1:
            continue
        toReturn.append(result[i])
        
    return toReturn

#added by sebastian
def center(x, y):
    #q
    if x in range(6,55) and y in range(6,55):
        return [30 ,30]
    #w
    elif x in range(61,110)  and y in range(6,55):
        return [85 ,30]
    #e
    elif x in range(117,166) and y in range(6,55):
        return [141, 30]
    #r
    elif x in range(171,220) and y in range(6,55):
        return [195, 30]
    #t
    elif x in range(227,276) and y in range(6,55):
        return [251, 30]
    #y
    elif x in range(282,331) and y in range(6,55):
        return [306,30]
    #u
    elif x in range(337,386) and y in range(6,55):
        return [361,30]
    #i
    elif x in range(393,442) and y in range (6,55):
        return [417,30]
    #o
    elif x in range(448,497) and y in range (6,55):
        return [472,30]
    #p
    elif x in range(504,553) and y in range (6,55):
        return [528,30]
    #a
    elif x in range( 61,110) and y in range (58,107):
        return [85,82]
    #s
    elif x in range(117,166) and y in range (58,107):
        return [141, 82]
    #d
    elif x in range(171,220) and y in range (58,107):
        return [195, 82]
    #f
    elif x in range(227,276) and y in range (58,107):
        return [251, 82]
    #g
    elif x in range(282,331) and y in range (58,107):
        return [306, 82]
    #h
    elif x in range(337,386) and y in range (58,107):
        return [361, 82]
    #j
    elif x in range(393,442) and y in range( 58,107):
        return [417, 82]
    #k
    elif x in range(448,497) and y in range( 58,107):
        return [472, 82] 
    #l
    elif x in range(504,553) and y in range( 58,107):
        return [528, 82] 
    #z
    elif x in range( 61,110) and y in range(112,161):
        return [85 ,136] 
    #x
    elif x in range(117,166) and y in range(112,161):
        return  [141, 136] 
    #c
    elif x in range(171,220) and y in range(112,161):
        return [195, 136]
    #v
    elif x in range(227,276) and y in range(112,161):
        return [251, 136]
    #b
    elif x in range(282,331) and y in range(112,161):
        return [306, 136]
    #n
    elif x in range(337,386) and y in range(112,161):
        return [361, 136]
    #m
    elif x in range(393,442) and y in range(112,161):
        return [417, 136]

def dist(oldCoord, newCoord):
##    Written by Joe Banass
    return math.sqrt(math.pow((newCoord[0]-oldCoord[0]), 2)+math.pow((newCoord[1]-oldCoord[1]), 2))

def getTotalDistance(CBCurLineContainer):
##    Written by Joe Banass
    length = 0
    for i in range(len(CBCurLineContainer)):
        length += CBCurLineContainer[i][2]
    return length


#CALLBACK VARIABLES BELOW
CBIntervalIDContainer = []
CBCoordinatesContainer = [] # for appending to CBMainLineIDContainer
CBMainLineIDContainer = []  # keeps track of line item numbers to delete later
CBCurLineContainer = [] # (oldpoint.x, oldpoint.y), (newpoint.x, newpoint.y), dist(previous tuples listed))
CBTotalTextEntered = 0
#END CALLBACK VARIABLES

def callback(event, reset):
##    Written by Joe Banass
    global CBTotalTextEntered, CBCoordinatesContainer, CBMainLineIDContainer, CBIntervalIDContainer, CBCurLineContainer, canvas
    if reset == 1: #if we release the button
        for i in range(len(CBMainLineIDContainer)): #delete the CBCoordinatesContainer drawn
            canvas.delete(CBMainLineIDContainer[i])
        for i in range(len(CBIntervalIDContainer)):
            canvas.delete(CBIntervalIDContainer[i])
        if len(CBCoordinatesContainer) > 1: # if it was dragged
            results = [CBCoordinatesContainer[0][0],
                       CBCoordinatesContainer[0][1],
                       CBCoordinatesContainer[-1][0],
                       CBCoordinatesContainer[-1][1],
                       getTotalDistance(CBCurLineContainer)]
        else: #if it was clicked
            results = [event.x, event.y, 0, 0, 0]

        CBMainLineIDContainer = [] #empty our lists
        CBIntervalIDContainer = []
        CBCoordinatesContainer = []
        CBCurLineContainer = []

        first_centered = center(results[0], results[1]) #get the center of first letter of the word
        last_centered = center(results[2], results[3]) #get the center of last letter of the word
        length = results[4] #get length of user drawn line

        if (length == 0): #aka a keypress!
            for i in devKeyContainer:
                if first_centered[0] == i[1][0] and first_centered[1] == i[1][1]:
                    result.insert(CBTotalTextEntered, i[0])
                    CBTotalTextEntered += 1
                    break
        else: #its a word, send it!
            array = search(first_centered[0], first_centered[1],
               last_centered[0], last_centered[1],
               length, email, CBIntervalIDContainer)
            result.delete(0,END)
            result.insert(0,array[0])
            button1['text'] = array[1]
            button2['text'] = array[2]
            button3['text'] = array[3]
            button4['text'] = array[4]
            button5['text'] = array[5]
            
        return
    if (len(CBCoordinatesContainer)) == 0: #if we just started drawing
        CBCoordinatesContainer.append((event.x, event.y))
    else: #we're in the middle of drawing
        CBCurLineContainer.append(((CBCoordinatesContainer[-1][0],
                                    CBCoordinatesContainer[-1][1]),
                                   (event.x, event.y),
                                   dist((CBCoordinatesContainer[-1][0],
                                         CBCoordinatesContainer[-1][1]),
                                        (event.x, event.y))))
        CBMainLineIDContainer.append(canvas.create_line((CBCoordinatesContainer[-1][0],
                                                         CBCoordinatesContainer[-1][1]),
                                                        (event.x, event.y),
                                                        fill="red"))
        if len(CBMainLineIDContainer)%3 == 0:
            CBIntervalIDContainer.append(canvas.create_line((CBCoordinatesContainer[-1][0],
                                                             CBCoordinatesContainer[-1][1]),
                                                             (event.x, event.y),
                                                             fill="blue"))
        CBCoordinatesContainer.append((event.x, event.y))

def ButtonSwitch(button):
    global result
    temp = result.get()
    result.delete(0,END)
    result.insert(0, button['text'])
    button['text'] = temp


#MAIN GLOBAL VARIABLES BELOW
results = []    # this holds our returned value from callback once the user releases the mouse button
firstname = ""  # holds our user's first name
lastname = ""   # holds our user's last name
email = ""      # holds our user's email
password = ""   # holds our user's password
br = mechanize.Browser()
#END MAIN GLOBAL VARIABLES

#MAIN BELOW
if os.path.exists("userid.txt"):
    myfile = open("userid.txt",'r')
    info = myfile.readline()
    info = info.split(",")
    firstname = info[0]
    email = info[2]
    password = info[3]
    myfile.close()
else:
    myfile = open("userid.txt",'w')
    firstname = raw_input("Enter your first name: ")
    while len(firstname) == 0:
        print("Sorry, you must enter a name\n")
        firstname = raw_input("Enter your first name: ")
    lastname = raw_input("Enter a last name: ")
    while len(lastname) == 0:
        print("Sorry, you must enter a last name\n")
        lastname = raw_input("Enter a last name: ")
    email = raw_input("Enter your email: ")
    while len(email) == 0 || '@' not in email:
        print("Sorry, you must enter an email\n")
        email = raw_input("Enter your email: ")
    password = raw_input("Enter a password: ")
    while len(password) == 0:
        print("Sorry, you must enter a password\n")
        password = raw_input("Enter a password: ")
    print("Registering you now with {}, {}, {}, {} as the details".format(firstname, lastname, email, password))
    myfile.write("{},{},{},{}".format(firstname, lastname, email, password))
    myfile.close()

if isDev:
    for i in range(len(devKeyContainer)):
        print(devKeyContainer[i][1][0],devKeyContainer[i][1][1])
        devMode(devKeyContainer[i][1][0],devKeyContainer[i][1][1])
#END MAIN

#TK SETUP BELOW
root = Tk()
fcW = 560 #Frame and Canvas X #orig 560
fcH = 170 #Frame and Canvas Y #orig 170
cciX = 279 # Canvas Create Image X #orig 279
cciY = 82 # Canvas Create Image Y #orig 82
root.geometry("560x230") #orig 560x220
result = Entry(root, font = ("Times", 14)) #create a results box
result.grid(row = 0, columnspan = 6) #put it in the window
userlabel = Label(root, text = email)
userlabel.grid(row = 0, column = 0, columnspan = 2)
button1 = Button(root, text = "")
button1.grid(row = 1, column = 0, columnspan = 2)
button1.bind("<Button>", func = lambda event : ButtonSwitch(button1))
button2 = Button(root, text = "")
button2.grid(row = 1, column = 1, columnspan = 2)
button2.bind("<Button>", func = lambda event : ButtonSwitch(button2))
button3 = Button(root, text = "")
button3.grid(row = 1, column = 2, columnspan = 2)
button3.bind("<Button>", func = lambda event : ButtonSwitch(button3))
button4 = Button(root, text = "")
button4.grid(row = 1, column = 3, columnspan = 2)
button4.bind("<Button>", func = lambda event : ButtonSwitch(button4))
button5 = Button(root, text = "")
button5.grid(row = 1, column = 4, columnspan = 2)
button5.bind("<Button>", func = lambda event : ButtonSwitch(button5))
image = Image.open("NewKeyboard.png")
photo = ImageTk.PhotoImage(image)
root.update() #update our root with new dimensions
frame = Frame(root, width = fcW, height = fcH) #create a frame in root
frame.grid(row = 2, columnspan = 6) #put it in the window
canvas = Canvas(frame, width = fcW, height = fcH) #create a canvas
canvas.create_image(cciX, cciY, image = photo) #put a image in the canvas
canvas.grid(row = 0, column = 0) #put it in the frame
canvas.bind("<B1-Motion>",func = lambda event: callback(event, 0), add = "+") #used to be B1-Motion
canvas.bind("<ButtonRelease-1>", func = lambda event: callback(event, 1))
root.mainloop()
#END TK SETUP
