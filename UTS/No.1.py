# Nama  : Durotun Nafisah Amalia Ahli
# NIM   : 20051397041
# Kelas : Manajemen Informatika 2020A
# UTS Grafkom No. 1 (Algoritma Garis Bresenham)

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

    glColor3f(12, 11, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(-7.50, 5.00)
    glVertex2f(0.0, 0.60)
    glVertex2f(4.90, 9.00)
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutCreateWindow("GRAFKOM")
glutDisplayFunc(draw)
glutMainLoop()