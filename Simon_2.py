##############################################
# Wes Cratty
# Lab 7
# CSCI 232: Data Structures & Algorithms
# 11/20/13
#
# Simon2.py
#---------------------------------------------
# This program simulates the "Simon" game from the
# 80's or 90's
##############################################
# added test commentkjhg
import tkinter as tk
import random
import tkinter.ttk as ttk
import time
import turtle
import file_io

roundList= list()
rounds =0
choices = ['red', 'green', 'blue', 'yellow','white', 'black']
fontSize= '20'
delay= .5
points = 0
flashSpeed =.5
index =0
sheldon = turtle.Turtle()
inputs =0
reduce =.1
at =0
fifty=50
difficult =False
name = "Player 1 "
winning = True
cList = list()
listScores ={}

def clear():
    screen = sheldon.getscreen()
    screen.clear()
    
def writeScores(points,name):
    global listScores
    player =False
    hight =300
    fontSize='20'
    listScores=file_io.read("listScores.csv")

    for (score, pName) in listScores.items():
        listScores[score] = pName.replace('+',"")

    
    if points > 0:
        listScores[points] = " +++++ "+name+" +++++ "
        
    title(hight,fontSize)
    
    for (score, pName) in sorted(listScores.items(),reverse=True):
       # pName = pName.replace('+',"")
        hight =hight -60
        sheldon.penup()
        sheldon.goto(-200,hight)
        sheldon.pendown()
        sheldon.color("black")
        instructions = str(score)+str(pName)
        sheldon.write(instructions, font=("Arial", fontSize, "normal"))

        
def title(hight,fontSize):

    sheldon.penup()
    sheldon.goto(-200,hight)
    sheldon.pendown()
    sheldon.color("black")
    instructions =" Top Scores:"
    sheldon.write(instructions, font=("Arial", fontSize, "normal"))

def write(l,hight =150):
    
    global points
    global name
    global fontSize
    global rounds
    if l=='rules':
        instructions ="Rules:\n"+\
                       " Simon is a classic electronic game from the 1980s \n"+\
                       "that presents the player with a sequence of lights \n"+\
                        "(in one of four different colors) in increasingly\n"+\
                        "rapid succession and number, and the player\n"+\
                        "is expected to repeat them back in the same order."
    elif l=='hard':
        fontSize = '20'
        instructions ="Difficult Rules:\n"+\
                       "Same rules apply except ignore the color\n"+\
                       "and follow the word. In addition the\n"+\
                       "order of colors are rearranged each round"

    elif l=='b':
        instructions =scores()
    elif l=='r':
        fontSize = '50'
        instructions ="Round "+str(rounds+1)

    elif l =='O':
        
        fontSize = '50'
        instructions = "Game over",scores()
        writeScores(points,name)
        writeFile()
        
    else:
        instructions =l
    if l=='O':
        pass
    else:
        
        sheldon.penup()
        sheldon.goto(-200,hight)
        clear()
        sheldon.pendown()
        sheldon.color("black")
        sheldon.write(instructions, font=("Arial", fontSize, "normal"))
        sheldon.penup()
        
def disable():
    button1.config(state='disabled')
    button2.config(state='disabled')
    button3.config(state='disabled')
    button4.config(state='disabled')
def enable():
    button.config(state='normal')
    button1.config(state='normal')
    button2.config(state='normal')
    button3.config(state='normal')
    button4.config(state='normal')
def scores():
    highScores = "43"
    return highScores , name, points

def ifs(colour):
    global index
    global points
    global winning
    global inputs
    
    
    if choices[cList[index]] == colour:
        points +=1
        update()
        inputs +=1
        index +=1
    else:
        root['bg'] = 'black'
        winning =False
        points -=1
        update()
        
    if rounds == inputs and winning:
        index =0
        flash()
    if winning ==False:
        disable()
        write('O')
        
def writeFile():
    global listScores
    names1 = []
        
    for (score, name2) in sorted(listScores.items()):
         names1.append(str(score) + "\t" + str(name2))

    ##   # Write the results to a file.
    file_io.write(names1,"listScores.csv")

    
def red():
    
    ifs('red')
    
def blue():
    
    ifs('blue')
    
def green():
    
    ifs('green')
    
def yellow():
    
    ifs('yellow')
      
def update():
    global  name,points
    name=inputStr.get()
    if difficult:
        name= name+" +++ Difficult"
    sf= str(name)+": Points: "+str(points)
    root.title(sf)

def startGame():
    
    global rounds
    global cList
    global name
    global flashSpeed
    global rounds
    global cList
    global index
    global inputs
    global winning
    global points
    global reduce 

    root['bg'] = 'purple'
    name = "Player 1 "
    inputs =0
    winning = True
    points = 0
    flashSpeed=2.0
    reduce = .1
    cList = list()
    instLbl1.config(fg='black')
    enable()
    update()
    makeNew()
    rounds = 0
    index =0
    flash()
    
def makeNew():
    
    global cList
    cList = list()
    newNum = random.randint(0,3)
    cList.append(newNum)
    while len(cList)< fifty:
        newNum = random.randint(0,3)
        if newNum != cList[len(cList)-1]:
            cList.append(newNum)
    

def flash():
    """  """
    global flashSpeed
    global rounds
    global cList
    global index
    global inputs
    global reduce
    
    write('r')
    time.sleep(flashSpeed)
    disable()

    update()
    index =0
    inputs =0
    flashSpeed =flashSpeed-reduce
    screen = sheldon.getscreen()
    screen.clear()
    rounds +=1
    i=0

    if difficult ==True:
        makeNew()
        reduce = .25
        while rounds > i:
            
            clear()
            screen.bgcolor(choices[cList[i+1]])
            instructions =str(choices[cList[i]])
            i+=1
            sheldon.penup()
            sheldon.goto(-200,300)
            sheldon.pendown()
            sheldon.color("black")
            sheldon.write(instructions, font=("Arial", fontSize, "normal"))
            sheldon.penup()
            time.sleep(flashSpeed)
    else:
        while rounds > i:
            
            screen.bgcolor(choices[cList[i]])
            i+=1

            time.sleep(flashSpeed)
    clear()
    enable()
    
def exit1():
    exit()
    
def diff():
    global difficult
    if difficult:
        difficult=False
        button5.config(text='Normal on')
        
    else:
        
        difficult =True
        button5.config(text='Difficult on')
        write('hard')
    
##------------------------------- Gui -----------------------------------
    
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (720, 180, 360, 600))
root.title("'You have 0 points'")
var = tk.StringVar(root)


write('rules')
labelText = tk.StringVar(root)
labelText.set('Enter Your Name')
instLbl1=tk.Label(root, textvariable=labelText, width=600)
instLbl1.config(bg='purple')

instLbl1.pack()


inputStr = tk.StringVar(root)
inputStr.set("Player 1")

inputStr_entry = tk.Entry(root, width=20, textvariable=inputStr)
inputStr_entry.pack()

button = tk.Button(root, text="Start Game", command=startGame)
button.pack(side='left', padx=30, pady=10)


button1 = tk.Button(root, text="red", command=red)
button1.pack(side='left', padx=10, pady=10)

button2 = tk.Button(root, text="Blue", command=blue)
button2.pack(side='left', padx=10, pady=10)

button3 = tk.Button(root, text="Yellow", command=yellow)
button3.pack(side='left', padx=10, pady=10)

button4 = tk.Button(root, text="Green", command=green)
button4.pack(side='left', padx=10, pady=10)

button5 = tk.Button(root, text="Normal on", command=diff)
button5.pack(side='left', padx=20, pady=10)

button6 = tk.Button(root, text="Exit", command=exit1)
button6.pack(side='left', padx=20, pady=10)


button1.config(state='disabled')
button2.config(state='disabled')
button3.config(state='disabled')
button4.config(state='disabled')
root.mainloop()






