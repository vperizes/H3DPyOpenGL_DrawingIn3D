import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *
from Camera import *


pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')
mesh = LoadMesh("cube.obj", GL_LINE_STRIP)
cube = Cube(GL_LINE_LOOP)
camera = Camera()

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0)


def camera_init():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update_camera(screen.get_width(), screen.get_height())


def draw_world_axes():
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(1, 0, 0)  # red color for x-axis
    glVertex3d(-1000, 0, 0)  # neg x
    glVertex3d(1000, 0, 0)  # pos x
    glColor(0, 1, 0)  # green color for y-axis
    glVertex3d(0, -1000, 0)
    glVertex3d(0, 1000, 0)
    glColor(0, 0, 1)  # blue color for z-axis
    glVertex3d(0, 0, -1000)
    glVertex3d(0, 0, 1000)
    glEnd()

    # sphere indicating pos x
    sphere = gluNewQuadric()
    glColor(1, 0, 0)
    glPushMatrix()
    glTranslated(1, 0, 0)  # adding glPush and glPop so that glTranslated does not effect the next sphere
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # sphere indicating pos y
    glColor(0, 1, 0)
    glPushMatrix()
    glTranslated(0, 1, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # sphere indicating pos y
    glColor(0, 0, 1)
    glPushMatrix()
    glTranslated(0, 0, 1)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # Color and line width for cube
    glColor(1, 1, 1)
    glLineWidth(1)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera_init()
    draw_world_axes()
    # glPushMatrix()
    cube.draw()
    # mesh.draw()
    # glPopMatrix()



done = False
initialise()
pygame.event.set_grab(True)  # grabs hold of mouse. Not usable for other windows when app is running
pygame.mouse.set_visible(False)  # mouse is no longer visible. Can't use it to shut window down --> program key press

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.set_grab(False)
                pygame.mouse.set_visible(True)
    display()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
