# Nama  : Durotun Nafisah Amalia Ahli
# NIM   : 20051397041
# Kelas : Manajemen Informatika 2020A
# UTS Grafkom No. 2 


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-7, 8, -3, 4, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.00, 4.00)
    glVertex2f(4.00, 4.00)
    glVertex2f(4.00, 0.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(0.00, 4.00)
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutCreateWindow("GRAFKOM")
glutDisplayFunc(draw)
glutMainLoop()
