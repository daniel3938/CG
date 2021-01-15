from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

n = 4
vertices = []
cores = []

r = 2
a = (2*math.pi)/n
for i in range(0,n):
    x = r*math.cos(a*i)
    y = 0    
    z = r*math.sin(a*i)
    vertices += [[x,y,z]]
    cores += [[random.random(),random.random(),random.random()]]

vertices += [[0,3,0]]
cores += [[random.random(),random.random(),random.random()]]
cores2 =( (random.random(),random.random(),random.random()),(random.random(),random.random(),random.random()) ) 

def Cubo():
    glBegin(GL_TRIANGLES)
    for i in range(0,n):
        glColor3fv((cores[i]))
        if i == n-1:
            glVertex3f(vertices[i][0],vertices[i][1],vertices[i][2])
            glVertex3f(vertices[0][0],vertices[0][1],vertices[0][2])
            glVertex3f(vertices[-1][0],vertices[-1][1],vertices[-1][2])
        else:
            glVertex3f(vertices[i][0],vertices[i][1],vertices[i][2])
            glVertex3f(vertices[i+1][0],vertices[i+1][1],vertices[i+1][2])
            glVertex3f(vertices[-1][0],vertices[-1][1],vertices[-1][2])
    glEnd()

    glBegin(GL_POLYGON)
    glColor3fv(cores2[0])
    for i in range(0,n):
        glVertex3f(vertices[i][0],vertices[i][1],vertices[i][2])
    glEnd()

a = 0

def desenhaDoisCubos():
    # Cubo da Esquerda
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(-a,-a,-a,-a)
    Cubo()
    glPopMatrix()
    # Cubo da Direita
    #glPushMatrix()
    #glTranslatef(2,0,0)
    #glRotatef(a,1,0,0)
    #Cubo()
    #glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0,0,0)
    desenhaDoisCubos()
    #glPopMatrix()
    #glPushMatrix()
    #glTranslatef(0,2,0)
    #desenhaDoisCubos()
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(20,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(20,timer,1)
glutMainLoop()


