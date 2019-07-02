import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as Textbox

import numpy as np

def figure():
    glPushMatrix()
  
    glBegin(GL_LINE_LOOP)
    counter = 0
    while counter < len(pointEntries):
        if(pointEntries[counter].get() != ""):
            glVertex3f(float(pointEntries[counter].get()) , float(pointEntries[counter + 1].get())  , float(pointEntries[counter + 2].get()))
        counter = counter + 3
    
    glEnd() 
    glPopMatrix()

    glColor3f(.5, .8, 1)
    #POINT DRAW
    glPushMatrix()
    glBegin(GL_POINTS)
    counter = 0
    while counter < len(pointEntries):
        if(pointEntries[counter].get() != ""):
            glVertex3f(float(pointEntries[counter].get()) , float(pointEntries[counter + 1].get())  , float(pointEntries[counter + 2].get()))
        counter = counter + 3
    
    glEnd() 
    glPopMatrix()

def showAxes(longitude):
    
    glPushMatrix()
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f( 0,0 ,0 )
    glVertex3f( longitude,0 ,0 )
    glEnd()
    glPopMatrix()


    
    glPushMatrix()
    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    glVertex3f( 0,0 ,0 )
    glVertex3f( 0,longitude ,0 )
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex3f( 0,0 ,0 )
    glVertex3f( 0, 0,longitude )
    glEnd()
    glPopMatrix()

    glPushMatrix()
    #glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(1,longitude):
        glColor3f(1, 1, 1)
        glVertex3f( i,0,0 )
        glVertex3f( 0, i,0 )
        glVertex3f( 0, 0,i )

    glEnd()
    glPopMatrix()
      

def translate(target):
    
    x = float(translateEntries[0].get() ) * target
    y = float(translateEntries[1].get() )* target
    z = float(translateEntries[2].get() )* target
    
    aux = (target * 10) - float(int(target * 10 ))

    if(aux < 0.01):
        temp = [x,y,z]
        translatePositions.append(temp)
    
    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    for i in range(len(translatePositions)): 
        glPushMatrix()
        glColor3f(1, 1, 1)
        glTranslatef(translatePositions[i][0], translatePositions[i][1], translatePositions[i][2])
        figure()
        glPopMatrix()
       
    glColor3f(1, 1, 0)
    glTranslatef(x,y,z)
    figure()
    glPopMatrix()



def rotate(target):
    x = float(rotateButtons[0].get())
    y = float(rotateButtons[1].get())
    z = float(rotateButtons[2].get())

    alpha = float(rotateEntry.get()) * target

    aux = (target * 10) - float(int(target * 10 ))

    if(aux < 0.01):
        temp = [x,y,z,alpha]
        rotatePositions.append(temp)
    

    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glRotatef(alpha, x,y,z)
    figure()
    glPopMatrix()

    for i in range(len(rotatePositions)): 
        glPushMatrix()
        glColor3f(1, 1, 1)
        glRotatef(rotatePositions[i][3] ,rotatePositions[i][0], rotatePositions[i][1], rotatePositions[i][2])
        figure()
        glPopMatrix()



def scale(target):
    x = float(scaleEntries[0].get())   
    y = float(scaleEntries[1].get()) 
    z = float(scaleEntries[2].get()) 


    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glScalef(x,y,z)
    figure()
    glPopMatrix()

def translate_rotate_scale(target):
    xT = float(translateEntries[0].get()) * target
    yT = float(translateEntries[1].get()) * target
    zT = float(translateEntries[2].get()) * target

    xR = float(rotateButtons[0].get())
    yR = float(rotateButtons[1].get())
    zR = float(rotateButtons[2].get())

    xS = float(scaleEntries[0].get()) 
    yS = float(scaleEntries[1].get()) 
    zS = float(scaleEntries[2].get()) 

    alpha = float(rotateEntry.get()) * target  

    aux = (target * 10) - float(int(target * 10 ))

    if(aux < 0.01):
        temp1 = [xT,yT,zT]
        translatePositions.append(temp1)
        temp2 = [xR,yR,zR,alpha]
        rotatePositions.append(temp2)

    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslate(xT,yT,zT)
    glRotatef(alpha, xR,yR,zR)
    glScalef(xS,yS,zS)
    figure()
    glPopMatrix()

    for i in range(len(rotatePositions)): 
        glPushMatrix()
        glColor3f(1, 1, 1)
        glRotatef(rotatePositions[i][3] ,rotatePositions[i][0], rotatePositions[i][1], rotatePositions[i][2])
        glTranslatef(translatePositions[i][0], translatePositions[i][1], translatePositions[i][2])    
        glScalef(xS,yS,zS)
        figure()
        glPopMatrix()

def translate_rotate(target):
    xT = float(translateEntries[0].get() ) * target
    yT = float(translateEntries[1].get() )* target
    zT = float(translateEntries[2].get() )* target

    xR = float(rotateButtons[0].get())
    yR = float(rotateButtons[1].get())
    zR = float(rotateButtons[2].get())

    alpha = float(rotateEntry.get()) * target

    aux = (target * 10) - float(int(target * 10 ))

    if(aux < 0.01):
        temp1 = [xT,yT,zT]
        translatePositions.append(temp1)
        temp2 = [xR,yR,zR,alpha]
        rotatePositions.append(temp2)

    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glRotatef(alpha, xR,yR,zR)
    glTranslate(xT,yT,zT)
    figure()
    glPopMatrix()

    for i in range(len(rotatePositions)): 
        glPushMatrix()
        glColor3f(1, 1, 1)
        glRotatef(rotatePositions[i][3] ,rotatePositions[i][0], rotatePositions[i][1], rotatePositions[i][2])
        glTranslatef(translatePositions[i][0], translatePositions[i][1], translatePositions[i][2])
        figure()
        glPopMatrix()

def translate_scale(target):
    xT = float(translateEntries[0].get() ) * target
    yT = float(translateEntries[1].get() )* target
    zT = float(translateEntries[2].get() )* target


    xS = float(scaleEntries[0].get())  
    yS = float(scaleEntries[1].get()) 
    zS = float(scaleEntries[2].get()) 

    aux = (target * 10) - float(int(target * 10 ))

    if(aux < 0.01):
        temp = [xT,yT,zT]
        translatePositions.append(temp)

     

    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslate(xT,yT,zT)
    glScalef(xS,yS,zS)
    figure()
    glPopMatrix()

    for i in range(len(translatePositions)): 
        glPushMatrix()
        glColor3f(1, 1, 1)
        glTranslatef(translatePositions[i][0], translatePositions[i][1], translatePositions[i][2])
        glScalef(xS,yS,zS)
        figure()
        glPopMatrix()

def rotate_scale(target):
  
    xR = float(rotateButtons[0].get())
    yR = float(rotateButtons[1].get())
    zR = float(rotateButtons[2].get())

    xS = float(scaleEntries[0].get())   
    yS = float(scaleEntries[1].get()) 
    zS = float(scaleEntries[2].get()) 

    alpha = float(rotateEntry.get()) * target  

    aux = (target * 10) - float(int(target * 10 ))

    if(aux < 0.01):
        temp = [xS,yS,zS,alpha]
        rotatePositions.append(temp)

    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)

    glRotatef(alpha, xR,yR,zR)
    glScalef(xS,yS,zS)
    figure()
    glPopMatrix()

    for i in range(len(rotatePositions)): 
        glPushMatrix()
        glColor3f(1, 1, 1)
        glRotatef(rotatePositions[i][3] ,rotatePositions[i][0], rotatePositions[i][1], rotatePositions[i][2])
        glScalef(xS,yS,zS)
        figure()
        glPopMatrix()

translatePositions = []
rotatePositions = []


def main():
    translatePositions.clear()
    rotatePositions.clear()
    inputvalidator = True

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)
    camX = camY = camZ = 0
    camX = float(cameraEntries[0].get())
    camY = float(cameraEntries[1].get())
    camZ = float(cameraEntries[2].get())

    longitude = int(max(camX,camY,camZ) * 2)
    tempLoop = loopVariable.get()
    print(tempLoop)
    if(tempLoop == 1):
        loop = True
    else:
        loop = False
  

    gluLookAt(camX, camY, camZ, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glPointSize(3)

    translateValidator = True
    for entry in translateEntries:
        if(entry.get() == ''):
            translateValidator = False

    rotateValidator = True
    if( rotateEntry.get() == ''):
        rotateValidator = False


    scaleValidator = True
    for entry in scaleEntries:
        if(entry.get() == ''):
            scaleValidator = False
    
    target = 0.0
    operation = 1
    targetOperation = 0
    #Display funtion
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        showAxes(longitude)

        if(target < 1): 
            target += 0.001
        else:
            target = 1

        if(translateValidator and rotateValidator and scaleValidator):
            translate_rotate_scale(target) 
        elif(translateValidator and rotateValidator ):
            translate_rotate(target)
        elif(translateValidator and scaleValidator):
            translate_scale(target)
        elif(rotateValidator and scaleValidator):
            rotate_scale(target)
        elif(translateValidator):
            translate(target)
        elif(rotateValidator):
            rotate(target)
        elif(scaleValidator):
            scale(target)
        else:
            figure()

        if(target > 1 and loop):
            translatePositions.clear()
            rotatePositions.clear()
            target = 0
            operation = operation + 1
            if(operation >= targetOperation):
                operation = 1
        
        
        pygame.display.flip()
        pygame.time.wait(10)





window = Tk()
window.title('Graphic Simulator')
window.geometry('850x1000')

pointLabels = ['x' , 'y', 'z']



#Top Input
top_frame = ttk.Frame(window)
top_frame.grid(column = 0, row = 0, sticky='N',pady='10',  columnspan=2)
points_label = ttk.Label(top_frame, text ="Points")
points_label.grid(column = 0, row = 0, sticky='W',pady='10',  columnspan=1)

for i in range(1,4):
    pointLabel = ttk.Label(top_frame, text =pointLabels[i-1])
    pointLabel.grid(column = i, row = 0, sticky='N',pady='10',  columnspan=1)


pointEntries = []
for i in range(1,5):
    points_label = ttk.Label(top_frame, text =i)
    points_label.grid(column = 0, row = i, sticky='W',pady='10',  columnspan=1)
    for j in range(3) :
       
        entry = Entry(top_frame) 
        entry.grid(column = j + 1, row = i, sticky='W',pady='10',   columnspan=1) 
        pointEntries.append(entry)

#camera
camera_frame = ttk.Frame(window)
camera_frame.grid(column = 2, row = 0, sticky='N',pady='10',  columnspan=1)
camera_label = ttk.Label(camera_frame, text ="Camera")
camera_label.grid(column = 0, row = 0, sticky='W',pady='10',  columnspan=1)

cameraEntries = []
for i in range(1,4):
    label = ttk.Label(camera_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='W',pady='10',  columnspan=1)
    entry= Entry(camera_frame)
    entry.grid(column = 1, row = i, sticky='W',pady='10',  columnspan=1)
    cameraEntries.append(entry)


#Trasnlate 
translate_frame = ttk.Frame(window)
translate_frame.grid(column = 0, row =1 , sticky='N',pady='10', padx='20' , columnspan=1)
translate_label = ttk.Label(translate_frame, text="Translation")
translate_label.grid(column = 0, row = 0, sticky='N',pady='10',  columnspan=1)

translateEntries = []
for i in range(1,4):
    label = ttk.Label(translate_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='N',pady='10',  columnspan=1)
    entry = Entry(translate_frame)
    entry.grid(column = 1, row = i, sticky='N',pady='10',  columnspan=1)  
    translateEntries.append(entry)
    
#Rotate
rotate_frame = ttk.Frame(window)
rotate_frame.grid(column = 1, row = 1, sticky='N',pady='10',  padx='20', columnspan=1)
rotate_label = ttk.Label(rotate_frame, text="Rotation")
rotate_label.grid(column = 0, row = 0, sticky='N',pady='10',  columnspan=1)

rotateButtons = []
for i in range(1,4):
    label = ttk.Label(rotate_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='N',pady='10',  padx='20', columnspan=1)
    rotateVariable= IntVar()
    checkButton= ttk.Checkbutton(rotate_frame, variable= rotateVariable)
    checkButton.grid(column = 1, row = i, sticky='N', pady='10')
    rotateButtons.append(rotateVariable)
label = ttk.Label(rotate_frame, text='Degree')
label.grid(column = 0, row = 4, sticky='N',pady='10',  padx='20', columnspan=1)
rotateEntry = Entry(rotate_frame) 
rotateEntry.grid(column = 1, row = 4, sticky='N',pady='10',   columnspan=1) 


#scale
scale_frame = ttk.Frame(window)
scale_frame.grid(column = 2, row = 1, sticky='N',pady='10',  columnspan=1)
scale_label = ttk.Label(scale_frame, text="Scale")
scale_label.grid(column = 0, row = 0, sticky='N',pady='10',  columnspan=1)

scaleEntries = []
for i in range(1,4):
    label = ttk.Label(scale_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='W',pady='10',  columnspan=1)
    entry= Entry(scale_frame)
    entry.grid(column = 1, row = i, sticky='W',pady='10',  columnspan=1)
    scaleEntries.append(entry)


submitButton = ttk.Button(window, text="Submit", command=main)
submitButton.grid(column = 1, row = 2, sticky='N',pady='10')

loopLabel = ttk.Label(camera_frame, text='Loop')
loopLabel.grid(column = 0, row = 5, sticky='N',pady='10',  padx='10', columnspan=1)
loopVariable= IntVar()
loopCheckButton= ttk.Checkbutton(camera_frame, variable= loopVariable)
loopCheckButton.grid(column = 1, row = 5, sticky='N', pady='10')

window.mainloop()
    


main()