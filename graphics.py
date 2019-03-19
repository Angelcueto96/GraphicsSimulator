import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as Textbox

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
    
      

    



x = 0.0
y = 0.0
z = 0.0
    
def reshape(x, y):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(x) / float(y), 0.1, 200.0)
    glMatrixMode(GL_MODELVIEW)
    glViewport(0, 0, x, y)
    gluLookAt(0.0, 1.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    display()

def idle():
    glutPostRedisplay()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)

    '''
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(45.0, float(x) / float(y), 0.1, 200.0)
    glMatrixMode(GL_MODELVIEW)
    glViewport(0, 0, display[0], display[1])
    #gluLookAt(0.0, 1.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    '''
    '''
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB)
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutMainLoop()
    
    
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(1.5, 1.5, 1.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    '''
    gluLookAt(6, 6, 6, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        
        x = float(translate_x.get())

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glTranslatef(x,y,z)
        Cube(3)
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)





window = Tk()
window.title('Graphic Simulator')
window.geometry('700x700')
    
label_translate = ttk.Label(window, text="Translation")
label_translate.grid(column = 0, row = 0, sticky='W',pady='20',  columnspan=10)
translate_x = Entry(window)
translate_x.grid(column = 0, row = 1, sticky='W',pady='20',  columnspan=10)
    
submitButton = ttk.Button(window, text="Submit", command=main)
submitButton.grid(column = 0, row = 2, sticky='W',pady='20',  columnspan=10)

window.mainloop()
    


 

    

main()