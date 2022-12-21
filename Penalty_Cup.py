from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np

def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(255, 140, 0)
    glVertex2f(x, y)
    glEnd()


def Circlepoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)


def midPointCircle(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    Circlepoints(x, y, x0, y0)  # Circlepoints(x+x0,y+y0)

    while (x < y):

        if d < 0:
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        Circlepoints(x, y, x0, y0)


def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #eightWayCircle(370, 400, 15) # ftbll

    #eightWayCircle(350, 550, 10)
    eightWayCircle(320, 470, 10)  # pessi er khoma
    #findZone(230, 250, 230, 220) # useless
    findZone(320, 465, 320, 420) # pessir pet
    findZone(320, 420, 290, 369) # pessi er hogar side
    findZone(320, 465, 305, 420) # mathar side
    findZone(320, 420, 355, 347) # pa
    findZone(320, 465, 350, 440) # hat
    # drawing post
    findZone(200, 750, 600, 750) # up
    findZone(200, 750, 200, 600) # left
    findZone(600, 750, 600, 600) # right
    findZone(0, 600, 900, 600) # ground line
    # placing targets?
    # top r8
    #findZone(550, 750, 600, 750)
    findZone(550, 750, 550, 700)
    findZone(550, 700, 600, 700)
    #a = eightWayCircle(580, 720, 10)
    # bottom r8
    findZone(550, 600, 550, 650)
    findZone(550, 650, 600, 650)
    #b = eightWayCircle(580, 620, 10)
    #top left
    findZone(250, 750, 250, 700)
    findZone(200, 700, 250, 700)
    #c = eightWayCircle(220, 720, 10)
    #bottom left
    findZone(250, 600, 250, 650)
    findZone(200, 650, 250, 650)
    #d = eightWayCircle(220, 630, 10)
    # centre
    findZone(400, 700, 450, 700)
    findZone(400, 650, 450, 650)
    findZone(400, 650, 400, 700)
    findZone(450, 650, 450, 700)

    # scalling center
    r = np.array([[400, 700, 0],
                  [450, 700, 0],
                  [0, 0, 1]])
    sc = 0.81
    vr = sc * r
    findZone(vr[0][0], vr[0][1], vr[1][0], vr[1][1])
    s = np.array([[sc, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])
    rs = np.matmul(r,s)
    findZone(rs[0][0], rs[0][1], rs[1][0], rs[1][1])
    r1 = np.array([[400, 650, 0],
                  [450, 650, 0],
                  [0, 0, 1]])
    rs1 = np.matmul(r1,s)
    findZone(rs1[0][0], rs1[0][1], rs1[1][0], rs1[1][1])
    r2 = np.array([[400, 650, 0],
                  [400, 700, 0],
                  [0, 0, 1]])
    rs2 = np.matmul(r2,s)
    findZone(rs2[0][0], rs2[0][1], rs2[1][0], rs2[1][1])
    r3 = np.array([[450, 650, 0],
                   [450, 700, 0],
                   [0, 0, 1]])
    rs3 = np.matmul(r3, s)
    findZone(rs3[0][0], rs3[0][1], rs3[1][0], rs3[1][1])



    n = int(input('where u want to shoot?'))
    if n == 0 :
        eightWayCircle(370, 400, 15) # ftbll
        print('Ready to shoot')
    if n == 1 :
        eightWayCircle(580, 720, 10)
        print('goal in the top right corner')
    if n == 2:
        eightWayCircle(580, 620, 10)
        print('goal in the bottom right corner')
    if n == 3:
        eightWayCircle(220, 720, 10)
        print('goal in the top left corner')
    if n == 4:
        eightWayCircle(220, 630, 10)
        print('goal in the bottom left corner')
    if n == 5:
        eightWayCircle(420, 680, 10)
        print('goal in the center')
    if n == 6:
        eightWayCircle(380, 620, 10)
        print('missed')
    if n == 7:
        eightWayCircle(220, 760, 10)
        print('missed')
    if n == 8:
        eightWayCircle(150, 700, 10)
        print('pessi missed')
    if n == 9:
        eightWayCircle(680, 720, 10)
        print('missed')
    if n == 10:
        eightWayCircle(350, 550, 10)
        eightWayCircle(220, 630, 10)
        print('Perfect shoot...')
    if n == 11:
        eightWayCircle(350, 550, 10)
        eightWayCircle(580, 620, 10)
        print('Perfect shoot...')




    glutSwapBuffers()


def eightWayCircle(x, y, radius):
    midPointCircle(x, y, radius)  # created big one

#----------------------------------------------------------------------------------------------------

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    if dx == 0:
        dx = 1

    if dy == 0:
        dy = -1

    if abs(dy) > abs(dx):
        if dx > 0 and dy > 0:
            zone = 1

        elif dx < 0 and dy > 0:
            zone = 2

        elif dx < 0 and dy < 0:
            zone = 5

        elif dx > 0 and dy < 0:
            zone = 6


    else:
        if dx > 0 and dy > 0:
            zone = 0

        elif dx < 0 and dy > 0:
            zone = 3

        elif dx < 0 and dy < 0:
            zone = 4

        elif dx > 0 and dy < 0:
            zone = 7

    converttoZone0(x0, y0, x1, y1, zone)


def converttoZone0(x0, y0, x1, y1, zone):
    X0 = x0
    Y0 = y0
    X1 = x1
    Y1 = y1

    if zone == 0:
        x_0 = X0
        y_0 = Y0
        x_1 = X1
        y_1 = Y1

    elif zone == 1:
        x_0 = Y0
        y_0 = X0
        x_1 = Y1
        y_1 = X1

    elif zone == 2:
        x_0 = Y0
        y_0 = -X0
        x_1 = Y1
        y_1 = -X1

    elif zone == 3:
        x_0 = -X0
        y_0 = Y0
        x_1 = -X1
        y_1 = Y1

    elif zone == 4:
        x_0 = -X0
        y_0 = -Y0
        x_1 = -X1
        y_1 = -Y1

    elif zone == 5:
        x_0 = -Y0
        y_0 = -X0
        x_1 = -Y1
        y_1 = -X1

    elif zone == 6:
        x_0 = -Y0
        y_0 = X0
        x_1 = -Y1
        y_1 = X1

    elif zone == 7:
        x_0 = X0
        y_0 = -Y0
        x_1 = X1
        y_1 = -Y1

    midpointlinealgo(x_0, y_0, x_1, y_1, zone)


def midpointlinealgo(x_0, y_0, x_1, y_1, zone):
    dX = x_1 - x_0
    dY = y_1 - y_0

    if dX == 0:
        dX = 1

    if dY == 0:
        dY = -0.5

    d = 2 * dY - dX
    incrNE = 2 * (dY - dX)
    incrE = 2 * dY

    X = x_0
    Y = y_0

    while X < x_1:

        if d > 0:
            d = d + incrNE
            Y = Y + 1
            X = X + 1
        else:
            d = d + incrE
            X = X + 1

        originalzone(X, Y, zone)


def originalzone(X, Y, zone):
    if zone == 0:
        x = X
        y = Y
        draw_points(x, y)

    if zone == 1:
        x = Y
        y = X
        draw_points(x, y)

    if zone == 2:
        x = -Y
        y = X
        draw_points(x, y)

    if zone == 3:
        x = -X
        y = Y
        draw_points(x, y)

    if zone == 2:
        x = -Y
        y = X
        draw_points(x, y)

    if zone == 5:
        x = -Y
        y = -X
        draw_points(x, y)

    if zone == 6:
        x = Y
        y = -X
        draw_points(x, y)

    if zone == 7:
        x = X
        y = -Y
        draw_points(x, y)



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(650, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Penalty_Cup")
glutDisplayFunc(screen)

glutMainLoop()