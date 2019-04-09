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
top_frame.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=1)
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

points_label_x1 = ttk.Label(top_frame, text="x1")
points_label_x1.grid(column = 0, row = 1, sticky='W',pady='20', padx='20', columnspan=1)
points_x1 = Entry(top_frame)
points_x1.grid(column = 1, row = 1, sticky='W',pady='20',   columnspan=1)
points_label_y1 = ttk.Label(top_frame, text="y1")
points_label_y1.grid(column = 2, row = 1, sticky='N',pady='20', padx='20', columnspan=1)
points_y1 = Entry(top_frame)
points_y1.grid(column = 3, row = 1, sticky='W',pady='20',  columnspan=1)
points_label_z1 = ttk.Label(top_frame, text="z1")
points_label_z1.grid(column = 4, row = 1, sticky='W',pady='20', padx='20', columnspan=1)
points_z1 = Entry(top_frame)
points_z1.grid(column = 5, row = 1, sticky='W',pady='20',  columnspan=1)

points_label_x2 = ttk.Label(top_frame, text="x2")
points_label_x2.grid(column = 0, row = 2, sticky='W',pady='20', padx='20', columnspan=1)
points_x2 = Entry(top_frame)
points_x2.grid(column = 1, row = 2, sticky='W',pady='20',   columnspan=1)
points_label_y2 = ttk.Label(top_frame, text="y2")
points_label_y2.grid(column = 2, row = 2, sticky='N',pady='20', padx='20', columnspan=1)
points_y2 = Entry(top_frame)
points_y2.grid(column = 3, row = 2, sticky='W',pady='20',  columnspan=1)
points_label_z2 = ttk.Label(top_frame, text="z2")
points_label_z2.grid(column = 4, row = 2, sticky='W',pady='20', padx='20', columnspan=1)
points_z2 = Entry(top_frame)
points_z2.grid(column = 5, row = 2, sticky='W',pady='20',  columnspan=1)

points_label_x3 = ttk.Label(top_frame, text="x3")
points_label_x3.grid(column = 0, row = 3, sticky='W',pady='20', padx='20', columnspan=1)
points_x3 = Entry(top_frame)
points_x3.grid(column = 1, row = 3, sticky='W',pady='20',   columnspan=1)
points_label_y3 = ttk.Label(top_frame, text="y3")
points_label_y3.grid(column = 2, row = 3, sticky='N',pady='20', padx='20', columnspan=1)
points_y3 = Entry(top_frame)
points_y3.grid(column = 3, row = 3, sticky='W',pady='20',  columnspan=1)
points_label_z3 = ttk.Label(top_frame, text="z2")
points_label_z3.grid(column = 4, row = 3, sticky='W',pady='20', padx='20', columnspan=1)
points_z3 = Entry(top_frame)
points_z3.grid(column = 5, row = 3, sticky='W',pady='20',  columnspan=1)
'''

#Trasnlate 
translate_frame = ttk.Frame(window)
translate_frame.grid(column = 0, row =1 , sticky='W',pady='20',  columnspan=1)
translate_label = ttk.Label(translate_frame, text="Translation")
translate_label.grid(column = 0, row = 0, sticky='W',pady='20',  columnspan=1)

translate_label_x = ttk.Label(translate_frame, text="x")
translate_label_x.grid(column = 0, row = 1, sticky='W',pady='20',  columnspan=1)
translate_x = Entry(translate_frame)
translate_x.grid(column = 1, row = 1, sticky='W',pady='20',  columnspan=1)

translate_label_y = ttk.Label(translate_frame, text="y")
translate_label_y.grid(column = 0, row = 2, sticky='W',pady='20',  columnspan=1)
translate_y = Entry(translate_frame)
translate_y.grid(column = 1, row = 2, sticky='W',pady='20',  columnspan=1)

translate_label_z = ttk.Label(translate_frame, text="z")
translate_label_z.grid(column = 0, row = 3, sticky='W',pady='20',  columnspan=1)
translate_z = Entry(translate_frame)
translate_z.grid(column = 1, row = 3, sticky='W',pady='20',  columnspan=1)

#Rotate
rotate_frame = ttk.Frame(window)
rotate_frame.grid(column = 1, row = 1, sticky='N',pady='20',  columnspan=1)
rotate_label = ttk.Label(rotate_frame, text="Rotation")
rotate_label.grid(column = 0, row = 0, sticky='N',pady='20',  columnspan=1)

rotate_label_x = ttk.Label(rotate_frame, text="x")
rotate_label_x.grid(column = 0, row = 1, sticky='N',pady='20',  columnspan=1)
rotate_x = Entry(rotate_frame)
rotate_x.grid(column = 1, row = 1, sticky='N',pady='20',  columnspan=1)

rotate_label_y = ttk.Label(rotate_frame, text="y")
rotate_label_y.grid(column = 0, row = 2, sticky='N',pady='20',  columnspan=1)
rotate_y = Entry(rotate_frame)
rotate_y.grid(column = 1, row = 2, sticky='N',pady='20',  columnspan=1)

rotate_label_z = ttk.Label(rotate_frame, text="z")
rotate_label_z.grid(column = 0, row = 3, sticky='N',pady='20',  columnspan=1)
rotate_z = Entry(rotate_frame)
rotate_z.grid(column = 1, row = 3, sticky='N',pady='20',  columnspan=1)


submitButton = ttk.Button(window, text="Submit", command=main)
submitButton.grid(column = 0, row = 4, sticky='W',pady='20',  columnspan=10)




window.mainloop()
    


 

    

main()