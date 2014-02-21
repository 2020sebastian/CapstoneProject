#########################################################
# basicGuiLayout.py                                     #
#                                                       #
# Maintainer:                                           #
#   Joe Banass                                          #
#   DePaul University                                   #
#   CSC 394 Capstone                                    #
#   Group 6                                             #
#                                                       #
#                                                       #
# This .py generates the gui, as well as providing an   #
# interface in which to insert text to a future web2py  #
# web interface                                         #
#                                                       #
#                                                       #
# Function Prototyping (in order of appearance)         #
#                                                       #
# devMode(key, coords)                                  #
#   - This function may become depreciated. It's main   #
#     function was to help create our input data for    #
#     generating the sokograph coordinate data. Trigger #
#     its use with changing the global variable devCoord#
#     to True                                           #
#                                                       #
# click(lambda event, string key)                       #
#   - records which key was pressed from gui            #
#                                                       #
# createArray()                                         #
#   - creates a key array based upon globalboolean value#
#     isQwerty and returns to the caller                #
#                                                       #
# keyAlgorithm(string[] keyArr)                         #
#   - creates the keys based upon gloabl variable       #
#     isQwerty (to make a qwerty keyboard or atomic     #
#     keyboard). keyArr houses our array of chars to    #
#     get our keys from                                 #
#                                                       #
# putKeys()                                             #
#    -simply initiates our program to begin creating our#
#       keys                                            #
#                                                       #
# setup()                                               #
#    - Helps create the sizing and constant position    #
#      of the window, depending on global boolean       #
#      variable isQwerty. Also sets timeToReset         #
#                                                       #
#########################################################


from Tkinter import Tk, Button, RAISED, Entry, END
import csv
import math


#initalize global vars for click method
isShift = False
isCaps = False
totalChars = 0 # to keep track of values entered
recordLst = []

#initialize global var for keyboard type
isQwerty = True

# DEVELOPMENT USE ONLY, DO NOT CHANGE
devCoord = False # DO NOT PUT THIS TO TRUE UNLESS YOU KNOW WHAT YOU ARE DOING
keyLst = [] # only use if devCoord is True
coordLst = []  # only use if devCoord is True

tupleList = [((0,0),(0,0),0)] # old point, new point, distance
lastLetterEntered = ""


## initiate Tkinter module and create window
root = Tk()

## create the output box and grid it
result = Entry(root, font = ('Times', 14))
result.grid(row = 6, columnspan = 9)

##############################################################
# FUNCTIONS BELOW                                            #
##############################################################

def devMode(key, coords):
##    This function may become depreciated. It\'s main 
##    function was to help create our input data for  
##    generating the sokograph coordinate data. Trigger 
##    its use with changing the global variable devCoord
##    to True
    global keyLst
    global coordLst
    if len(keyLst) == 0: # if our list is initially empty...
        keyLst.append(key) # we add the key to the list for tracking
        coordLst.append(coords) # and we append its coordinates in a tuple to a global lst for storage
    elif key != keyLst[-1]: # if a key isn't the previously entered key...
        # Then we assume input for current key is over with
        writer = csv.writer(open('coords.csv','ab'), delimiter=',') # we prepare our .csv coordinate file for writing...NOTE, it is "ab" so that it doesnt
                                                                    # put in an empty row between writing rows. Windows-specific problem apparently
                                                                    # IMPORTANT: CSV STRUCTURE IS AS FOLLOWS
        writer.writerow([keyLst[-1]] + [coordLst[0][0]] +           # Key, OriginX
                        [coordLst[0][1]] + [coordLst[1][0]] +       # OriginY, UpperLeftX
                        [coordLst[1][1]] + [coordLst[2][0]] +       # UpperLeftY, UpperRightX
                        [coordLst[2][1]] + [coordLst[3][0]] +       # UpperRightY, LowerLeftX
                        [coordLst[3][1]] + [coordLst[4][0]] +       # LowerLeftY, LowerRightX
                        [coordLst[4][1]])                           # LowerRightY
        keyLst.append(key) #we add the new key to the end
        coordLst = [] #we empty the coordinate list for new key coordinates
        coordLst.append(coords) #and we add the recently sent coordinates to the list
    else: #otherwise...We have the same key
        coordLst.append(coords) #we just add the coordinates to the list
    return
    
def dist(oldCoord, newCoord):
    return math.sqrt(math.pow((newCoord[0]-oldCoord[0]), 2)+math.pow((newCoord[1]-oldCoord[1]), 2))

def click(event, key):
##    records which key was pressed from gui
    ## MAY BECOME DEPRECIATED
    
    global isShift # boolean val
    global isCaps   # boolean val
    global totalChars # integer val
    global devCoord # boolean val
    

    #print(root.winfo_pointerxy()) #<---this displays current coordinates. Uncomment
                                        #to enable coordinate tracking

    
    if devCoord:
        devMode(key, root.winfo_pointerxy())
    
    
    if key == 'shift':
        isShift = True
        return
    elif key == 'caps':
        if isCaps:
            isCaps = False
        else:
            isCaps = True
        return
    elif key == 'enter':
        result.delete(0,END)
        return
    elif key == 'bsp':
        result.delete(totalChars-1, END)
        totalChars -= 1
        return
    elif key == '':
        return;

    totalChars += 1 # We passed the test cases, its safe to increment this value now!
    
    if isShift:
        key = key.capitalize()
        result.insert(END,key)
        isShift = False
    elif isCaps:
        key = key.capitalize()
        result.insert(END,key)
    else:
        result.insert(END,key)

    return

def createArray():
##    creates a key array based upon boolean value
##    and returns to the caller
    global isQwerty
    if isQwerty:
        keyArr = ['tab','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                  'caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';',
                  'shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',
                  'bsp', '!', '\'', '\"', '?', 'enter', 'NBest', '#', '\\']

        #11--->10--\
        #11--->10---\
        #-------------General row structure normalized to account for the indexing
        #11--->10---/
        #9---->8 --/

    else:
        keyArr = ['\'', 'b', 'k', 'd', 'g', '.', ',', '?', '!',
                      'tab', 'c', 'a', 'n', 'i', 'm', 'q', 'bsp',
                      'caps', 'f', 'l', 'e', '', 's', 'y', 'x', 'enter',
                      'shift', 'j', 'h', 't', 'o', 'p', 'v', 'NBest',
                      '@', '\\', ';', '\"', 'r', 'u', 'w', 'z', '#']

        #9--->8----\
        #8--->7-----\
        #9--->8-------General row structure normalized to account for the indexing
        #8--->7-----/
        #9--->8----/

    return keyArr

def spit(event, key):
    global tupleList
    global lastLetterEntered
    if key == lastLetterEntered:
        tupleList.append((tupleList[-1][1], root.winfo_pointerxy(), dist(tupleList[-1][1], root.winfo_pointerxy())))
        print("Recorded Data with the following: beginning = {} {}".format(key, tupleList[-1]))
    else:
        lastLetterEntered = key
        tupleList = [((0,0), root.winfo_pointerxy(), dist((0,0),root.winfo_pointerxy()))]
        print("Recorded new key Data with the following: beginning = {} {}".format(key, tupleList[-1]))

def keyAlgorithm(keyArr):
##    creates the keys based upon isQwerty (to make a   
##    qwerty keyboard or atomic keyboard). timeToReset  
##    exists to control when to change rows, and keyArr 
##    houses our strings of keys to grab from
    
    global isQwerty
    global timeToReset
    flag = True # We use this boolean value to know for Atomic Keyboards if our row has ended
    counter = 0 # We use this integer value to keep track of how many keys we have entered
    row = 0     # We use this integer value to allow for easy input of row number
    column = 0  # We use this integer value to allow for easy input of column number
    if isQwerty: # If we have a Qwerty Keyboard...
        for i in range(len(keyArr)):
            if keyArr[i] == '/': # We have our final row next!
                button = Button(master = root,
                                text = keyArr[i], # grabs key from keyArr
                                font = ('Times', 10),
                                padx = 10,
                                pady = 5,
                                relief = RAISED)
                button.grid(row = row, column = column) # bind it to the coordinates row and column
                button.bind('<Button>', func=lambda event, x = keyArr[i]:click(event,x), add="+")
                button.bind('<B1-Motion>', func = lambda event, x = keyArr[i]:spit(event, x), add="+")
                counter = 0 # reset our counter
                row += 1 # increase the row
                column = 0 # reset our columns
            else: # we dont have our last row here!
                button = Button(master = root,
                                text = keyArr[i], # grabs key from keyArr
                                font = ('Times', 10),
                                padx = 10,
                                pady = 5,
                                relief = RAISED)
                button.grid(row = row, column = column)
                button.bind('<Button>', func=lambda event, x = keyArr[i]:click(event,x), add="+")
                button.bind('<B1-Motion>', func = lambda event, x = keyArr[i]:spit(event, x), add="+")
                if counter == timeToReset: # are we at the end of our row?
                    counter = 0
                    row += 1
                    column = 0
                else:
                    counter += 1
                    column += 1
    else: # We have an Atomic Keyboard
        for i in range(len(keyArr)):
            if flag: # We have a large row!
                button = Button(master = root,
                                text = keyArr[i], # grabs key from keyArr
                                font = ('Times', 10),
                                padx = 10,
                                pady = 5,
                                relief = RAISED)
                button.grid(row = row, column = column) # bind it to the coordinates row and column
                button.bind('<Button>', func=lambda event, x = keyArr[i]:click(event,x), add="+")
                button.bind('<B1-Motion>', func = lambda event, x = keyArr[i]:spit(event, x), add="+")
                if counter == timeToReset: # are we at the end of our row?
                    counter = 0 # reset our counter
                    flag = False # reset our flag
                    row += 1 # increase the row
                    column = 0 # reset our columns
                    timeToReset = 7 # We have to change our timeToReset since Atomic Keyboards have an alternating row structure
                else:
                    counter += 1 # increase both our counter and column values, but not row!
                    column += 1
            else: # we dont have a large row here!
                button = Button(master = root,
                                text = keyArr[i], # grabs key from keyArr
                                font = ('Times', 10),
                                padx = 10,
                                pady = 5,
                                relief = RAISED)
                button.grid(row = row, column = column)
                button.bind('<Button>', func=lambda event, x = keyArr[i]:click(event,x), add="+")
                button.bind('<B1-Motion>', func = lambda event, x = keyArr[i]:spit(event, x), add="+")
                if counter == timeToReset: # are we at the end of our row?
                    counter = 0
                    flag = True
                    row += 1
                    column = 0
                    timeToReset = 8 # We have to change our timeToReset since Atomic Keyboards have an alternating row structure
                else:
                    counter += 1
                    column += 1
    return


def putKeys():
##    simply initiates our program to begin creating our
##    keys
    
    global isQwerty #used for determining which keyboard type to display

    keyArr = createArray() # Let's create our array of keys
    keyAlgorithm(keyArr)
    return

def setup():
##    Helps create the sizing and constant position    
##    of the window, depending on global boolean       
##    variable isQwerty. Also sets timeToReset
    
    global isQwerty
    global timeToReset
    global root

    #We have an if-statement here, since the Qwerty keyboad is a bit larger than the Atomic keyboard
    if isQwerty:
        root.geometry('480x200+400+300')
        timeToReset = 10  #refer to createArray comments as to why these values exist!
    else:
        root.geometry('400x200+440+300')
        timeToReset = 8
        
    #we update our root with new settings and return below back to main!
    root.update()
    return

##################################################################
#MAIN                                                            #
##################################################################

## Gets a lot of JUNK out of the way (window placement, resizing, etc)
setup()

## Add the keys
putKeys()

## Loop
root.mainloop()
    
