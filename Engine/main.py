import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
# from CubeMesh import *
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
mesh = LoadMesh("teapot.obj", GL_LINE_STRIP)
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


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera_init()
    glPushMatrix()
    mesh.draw()
    glPopMatrix()


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
