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
    
    
    glVertex3f(float(points_x1.get()) , float(points_y1.get()) , float(points_z1.get()) )
    glVertex3f(float(points_x2.get()) , float(points_y2.get()) , float(points_z2.get()) )
    glVertex3f(float(points_x3.get()) , float(points_y3.get()) , float(points_z3.get()) )
    
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
 
 
    
   

      

x = 0.0
y = 0.0
z = 0.0

def translate():
    x = float(translate_x.get())
    y = float(translate_y.get())
    z = float(translate_z.get())

    
    glColor3f(1, 1, 1)
    triangle()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslatef(x,y,z)
    triangle()
    glPopMatrix()

def rotate():
    x = float(rotate_x.get())
    y = float(rotate_y.get())
    z = float(rotate_z.get())

    glColor3f(1, 1, 1)
    triangle()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glRotatef(0,0,1, 90)
    triangle()
    glPopMatrix()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)

    gluLookAt(6, 6, 6, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    for ent in entries:
            print(ent.get())
    

    #Display funtion
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()

        


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        showAxes(10)
        '''
        if( points_x1.get() != '' and points_y1.get() != '' and points_z1.get() != '' and points_x2.get() != '' and points_y2.get() != '' and points_z2.get() != '' and points_x3.get() != '' and points_y3.get() != '' and points_z3.get() != ''):
            #triangle()
            #Cube(3)
            if(translate_x.get() != '' and translate_y.get() != '' and translate_z.get() != ''):
                translate()
            elif(rotate_x.get() != '' and rotate_y.get() != '' and rotate_z.get() != ''):
                rotate()
            else:
                Cube(3)
        '''
        
        
        pygame.display.flip()
        pygame.time.wait(10)





window = Tk()
window.title('Graphic Simulator')
window.geometry('700x700')
#Top Input
top_frame = ttk.Frame(window)
top_frame.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=3)
points_label = ttk.Label(top_frame, text ="Points")
points_label.grid(column = 0, row = 0, sticky='W',pady='10',  columnspan=1)

entries = []
for i in range(1,4):
    for j in range(3) :
        #label= ttk.Label(top_frame, text="x")
        #label.grid(column = j, row = i, sticky='W',pady='20', padx='20', columnspan=1)
        entry = Entry(top_frame) 
        entry.grid(column = j + 1, row = i, sticky='W',pady='20',   columnspan=1) 
        entries.append(entry)

'''

'''

#Trasnlate 
translate_frame = ttk.Frame(window)
translate_frame.grid(column = 0, row =1 , sticky='W',pady='20',  columnspan=1)
translate_label = ttk.Label(translate_frame, text="Translation")
translate_label.grid(column = 0, row = 0, sticky='W',pady='20',  columnspan=1)

for i in range(1,4):
    label = ttk.Label(translate_frame, text="x")
    label.grid(column = 0, row = i, sticky='W',pady='20',  columnspan=1)
    translate = Entry(translate_frame)
    translate.grid(column = 1, row = i, sticky='W',pady='20',  columnspan=1)
    
'''

'''


#Rotate
rotate_frame = ttk.Frame(window)
rotate_frame.grid(column = 1, row = 1, sticky='N',pady='20',  columnspan=1)
rotate_label = ttk.Label(rotate_frame, text="Rotation")
rotate_label.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=1)

for i in range(1,5):
    label = ttk.Label(rotate_frame, text="x")
    label.grid(column = 0, row = i, sticky='W',pady='20',  columnspan=1)
    translate = Entry(rotate_frame)
    translate.grid(column = 1, row = i, sticky='W',pady='20',  columnspan=1)


'''

'''

#scale
scale_frame = ttk.Frame(window)
scale_frame.grid(column = 2, row = 1, sticky='N',pady='20',  columnspan=1)
scale_label = ttk.Label(scale_frame, text="Scale")
scale_label.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=1)

for i in range(1,4):
    label = ttk.Label(scale_frame, text="x")
    label.grid(column = 0, row = i, sticky='W',pady='20',  columnspan=1)
    translate = Entry(scale_frame)
    translate.grid(column = 1, row = i, sticky='W',pady='20',  columnspan=1)



submitButton = ttk.Button(window, text="Submit", command=main)
submitButton.grid(column = 0, row = 4, sticky='W',pady='20',  columnspan=10)




window.mainloop()
    


 

    

main()