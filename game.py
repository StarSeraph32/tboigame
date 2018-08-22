from tkinter import *   #import tk and time
import time

#setup tk
myTk = Tk()
canvas = Canvas(myTk,width = 1080,height=720)
canvas.pack()
myTk.lift()
myTk.title("Tangerine Adventure!")
background = PhotoImage(file = "stanley's_car_crash_site.png")
canvas.create_image(0,0,anchor = NW, image = background)
player = PhotoImage(file = 'normal_stanley.png')
playerCharacter = canvas.create_image(100,350,image=player)
spawnPoint = canvas.coords(playerCharacter)
inventory = ['Rusted Knife']    #The inventory
#movement variables
moveup = False
movedown = False
moveright = False
moveleft = False
coords = canvas.coords(playerCharacter)
interactionText = None
interactionTextRect = None

#create a timer to use for various things
def clock(time):
    time.sleep(time)
#draw the river
riverWater = canvas.create_rectangle(350,0,530,720,fill='blue')
sandLeft = canvas.create_rectangle(320,0,350,720,fill='yellow')
sandRight = canvas.create_rectangle(530,0,560,720,fill='yellow')

#Controls movement
def keypress(event):      #Keypress detector
    global moveup,movedown,moveright,moveleft
    if event.keysym == "w":
        moveup = True
    if event.keysym == "s":
        movedown = True
    if event.keysym == "d":
        moveright = True
    if event.keysym == "a":
        moveleft = True
def keyrelease(event):    #Keyrelease detector
    global moveup,movedown,moveright,moveleft
    if event.keysym == "w":
        moveup = False
    if event.keysym == "s":
        movedown = False
    if event.keysym == "d":
        moveright = False
    if event.keysym == "a":
        moveleft = False
def movement():     #Moves the player depending on their keypresses
    global coords,playerCharacter,moveup,movedown,moveright,moveleft
    if isDrown:
        return
    coords = canvas.coords(playerCharacter)
    if coords[1] != 20:
        if moveup:
            canvas.move(playerCharacter,0,-2)
            if interactionText != None:
                canvas.move(interactionText, 0, -2)
                canvas.move(interactionTextRect, 0, -2)

    if coords[1] != 700:
        if movedown:
            canvas.move(playerCharacter,0,2)
            if interactionText != None:
                canvas.move(interactionText, 0, 2)
                canvas.move(interactionTextRect, 0, 2)
    if coords[0] != 1040:
        if moveright:
            canvas.move(playerCharacter,2,0)
            if interactionText != None:
                canvas.move(interactionText, 2, 0)
                canvas.move(interactionTextRect, 2, 0)
    if coords[0] != 40:
        if moveleft:
            canvas.move(playerCharacter,-2, 0)
            if interactionText != None:
                canvas.move(interactionText, -2, 0)
                canvas.move(interactionTextRect, -2, 0)

canvas.bind_all('<KeyPress>',keypress) #binds all keypresses to the keypress func
canvas.bind_all('<KeyRelease>',keyrelease) #binds all keyreleases to the keyrelease func

drownTextBox = canvas.create_rectangle(325,325,675,375,fill = 'white',state = HIDDEN)
drownText = canvas.create_text(500,350,text = 'You drowned! You should have listened to the guide...',fill='red',state=HIDDEN)
isDrown = False
def setDrownState(s):
    global drownText, isDrown

    canvas.itemconfig(drownText, state=s)
    canvas.itemconfig(drownTextBox, state=s)
    isDrown = (s == NORMAL)

#sends the player back to start when they go in the river 
def drown():
    global drownText,drownTextBox

    if not isDrown and coords[0] >= 320:
        setDrownState(NORMAL)
        canvas.after(5000, setDrownState, HIDDEN)
        canvas.itemconfig(playerCharacter,state = HIDDEN)
        curr_coords = canvas.coords(playerCharacter)
        canvas.move(playerCharacter, 100 - curr_coords[0], 350 - curr_coords[1])
        canvas.itemconfig(playerCharacter, state = NORMAL)
def checkInteraction(npcCoordsX1,npcCoordsY1,npcCoordsX2,npcCoordsY2):
    global coords, interactionText,moveleft
    cornerDetect1 = False
    cornerDetect2 = False
    if coords[0] >= npcCoordsX1 and coords[0] >= npcCoordsY1:
        cornerDetect1 = True
    elif interactionText != None and coords[0] < npcCoordsX1 and coords[0] < npcCoordsY1:
        cornerDetect1 = False
    if coords[0] <= npcCoordsX2 and coords[1] <= npcCoordsY2:
        cornerDetect2 = True
    elif interactionText != None and coords[0] > npcCoordsX2 and coords[1] > npcCoordsY2:
        cornerDetect2 = False
    if cornerDetect1 and cornerDetect2 and interactionText == None:
        interactionText = canvas.create_text(coords[0],coords[1],text='PRESS SPACE TO INTERACT',fill='black')
        interactionTextRect = (canvas.create_rectangle(canvas.bbox(interactionText),fill='white'))
    elif not (cornerDetect1 and cornerDetect2) and interactionText != None:
        canvas.delete(interactionText)
        interactionText = None

    
#Different weapon classes
#class Sword:
 #   miss = 0
 #   def __init__(self, distance, attack, fireRate, defence, distance):
#        self.distance = distance
 #       self.attack = attack
  #      self.fireRate = fireRate
  #      self.defence = defence
  #      self.distance = distance

class Gun:
    attack = 4
    fireRate = 100
    defence = 1
    distance = 20
    miss = 10
class Shield:
    attack = 2
    fireRate = 60
    defence = 10
    distance = 5
    miss = 0
class Bow:
    attack = 6
    fireRate = 50
    defence = 2
    distance = 15
    miss = 5
while True:
    movement()
    drown()
    checkInteraction(0,0,50,100)
    myTk.update()
    time.sleep(0.015)
myTk.destroy()