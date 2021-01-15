from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    (1,-1,1),
    (1,-1,-1),
    (-1,-1,-1),
    (-1,-1,1),
    (0,1,0)
    )

linhas = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (0,4),
    (1,4),
    (2,4),
    (3,4)
    )

faces = (
    (0,1,2,3),
    (0,1,4),
    (1,2,4),
    (2,3,4),
    (3,0,4)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Cubo():
    glBegin(GL_QUADS)
    i = 0
    for face in faces[0]:
        glColor3fv(cores[i])
        #for vertex in face:
            #glColor3fv(cores[vertex])
         #   glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

a = 0

def desenhaDoisCubos():
    # Cubo da Esquerda
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(-a,0,0,1)
    Cubo()
    glPopMatrix()
    # Cubo da Direita
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(a,1,0,0)
    Cubo()
    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0,-2,0)
    desenhaDoisCubos()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,2,0)
    desenhaDoisCubos()
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

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
glutTimerFunc(50,timer,1)
glutMainLoop()


