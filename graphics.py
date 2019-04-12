import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as Textbox

import numpy as np

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube(hside):
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd() 
    
def triangle():
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    
    
    #glVertex3f(float(points_x1.get()) , float(points_y1.get()) , float(points_z1.get()) )
    #glVertex3f(float(points_x2.get()) , float(points_y2.get()) , float(points_z2.get()) )
    #glVertex3f(float(points_x3.get()) , float(points_y3.get()) , float(points_z3.get()) )
    
    glEnd() 

    glPopMatrix()
def figure():
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    
    counter = 0
    while counter < len(pointEntries):
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
 
      

def translate(target):
    
    x = float(translateEntries[0].get() ) * target
    y = float(translateEntries[1].get() )* target
    z = float(translateEntries[2].get() )* target

    
    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslatef(x,y,z)
    figure()
    glPopMatrix()

def rotate(target):
    print(rotateButtons[0].get())
    x = float(rotateButtons[0].get())
    y = float(rotateButtons[1].get())
    z = float(rotateButtons[2].get())

    alpha = float(rotateEntry.get()) * target
    

    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glRotatef(alpha, x,y,z)
    figure()
    glPopMatrix()

def scale(target):
    x = float(scaleEntries[0].get())  * target 
    y = float(scaleEntries[1].get()) * target  
    z = float(scaleEntries[2].get()) * target  


    glColor3f(1, 1, 1)
    figure()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glScalef(x,y,z)
    figure()
    glPopMatrix()


def main():
    inputvalidator = True

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)
    camX = camY = camZ = 0
    camX = float(cameraEntries[0].get())
    camY = float(cameraEntries[1].get())
    camZ = float(cameraEntries[2].get())

    gluLookAt(camX, camY, camZ, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    

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
    #Display funtion
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        showAxes(10)

         
        target += 0.001
        if(translateValidator):
            translate(target)
        elif(rotateValidator):
            rotate(target)
        elif(scaleValidator):
            scale(target)

        if(target > 1):
            target = 0
        
        
        pygame.display.flip()
        pygame.time.wait(10)





window = Tk()
window.title('Graphic Simulator')
window.geometry('850x1000')

pointLabels = ['x' , 'y', 'z']

#Top Input
top_frame = ttk.Frame(window)
top_frame.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=2)
points_label = ttk.Label(top_frame, text ="Points")
points_label.grid(column = 0, row = 0, sticky='W',pady='10',  columnspan=1)

for i in range(1,4):
    pointLabel = ttk.Label(top_frame, text =pointLabels[i-1])
    pointLabel.grid(column = i, row = 0, sticky='N',pady='10',  columnspan=1)


pointEntries = []
for i in range(1,4):
    points_label = ttk.Label(top_frame, text =i)
    points_label.grid(column = 0, row = i, sticky='W',pady='10',  columnspan=1)
    for j in range(3) :
        #label= ttk.Label(top_frame, text="x")
        #label.grid(column = j, row = i, sticky='W',pady='20', padx='20', columnspan=1)
        entry = Entry(top_frame) 
        entry.grid(column = j + 1, row = i, sticky='W',pady='20',   columnspan=1) 
        pointEntries.append(entry)

#camera
camera_frame = ttk.Frame(window)
camera_frame.grid(column = 2, row = 0, sticky='N',pady='20',  columnspan=1)
camera_label = ttk.Label(camera_frame, text ="Camera")
camera_label.grid(column = 0, row = 0, sticky='W',pady='10',  columnspan=1)

cameraEntries = []
for i in range(1,4):
    label = ttk.Label(camera_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='W',pady='20',  columnspan=1)
    entry= Entry(camera_frame)
    entry.grid(column = 1, row = i, sticky='W',pady='20',  columnspan=1)
    cameraEntries.append(entry)


#Trasnlate 
translate_frame = ttk.Frame(window)
translate_frame.grid(column = 0, row =1 , sticky='N',pady='20', padx='20' , columnspan=1)
translate_label = ttk.Label(translate_frame, text="Translation")
translate_label.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=1)

translateEntries = []
for i in range(1,4):
    label = ttk.Label(translate_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='N',pady='20',  columnspan=1)
    entry = Entry(translate_frame)
    entry.grid(column = 1, row = i, sticky='N',pady='20',  columnspan=1)  
    translateEntries.append(entry)
    
#Rotate
rotate_frame = ttk.Frame(window)
rotate_frame.grid(column = 1, row = 1, sticky='N',pady='20',  padx='20', columnspan=1)
rotate_label = ttk.Label(rotate_frame, text="Rotation")
rotate_label.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=1)

rotateButtons = []
for i in range(1,4):
    label = ttk.Label(rotate_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='N',pady='20',  padx='20', columnspan=1)
    rotateVariable= IntVar()
    checkButton= ttk.Checkbutton(rotate_frame, variable= rotateVariable)
    checkButton.grid(column = 1, row = i, sticky='N', pady='20')
    rotateButtons.append(rotateVariable)
label = ttk.Label(rotate_frame, text='Degree')
label.grid(column = 0, row = 4, sticky='N',pady='20',  padx='20', columnspan=1)
rotateEntry = Entry(rotate_frame) 
rotateEntry.grid(column = 1, row = 4, sticky='N',pady='20',   columnspan=1) 


#scale
scale_frame = ttk.Frame(window)
scale_frame.grid(column = 2, row = 1, sticky='N',pady='20',  columnspan=1)
scale_label = ttk.Label(scale_frame, text="Scale")
scale_label.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=1)

scaleEntries = []
for i in range(1,4):
    label = ttk.Label(scale_frame, text=pointLabels[i-1])
    label.grid(column = 0, row = i, sticky='W',pady='20',  columnspan=1)
    entry= Entry(scale_frame)
    entry.grid(column = 1, row = i, sticky='W',pady='20',  columnspan=1)
    scaleEntries.append(entry)


submitButton = ttk.Button(window, text="Submit", command=main)
submitButton.grid(column = 0, row = 4, sticky='W',pady='20')

window.mainloop()
    


 

    

main()