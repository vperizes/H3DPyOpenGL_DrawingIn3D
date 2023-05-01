from pygame.locals import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Transformations in Python')
cube = Cube(GL_LINE_LOOP)
mesh = LoadMesh("cube.obj", GL_LINE_LOOP)

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 500.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)  # this switches open GL to model view mode. Any operations after this line are applied
    # to model view matrix
    glLoadIdentity()
    # glTranslated(0, 0, -2)  # camera is sitting at origin looking down neg z-axis (neg z goes into screen) - need to
    # push model back to make it visible. Default: pos x is to the right and pos y is up
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslated(0, 1, -5)
    glRotated(45, 0, 1, 0)  # this rotates the object 45 degrees about the 0, 1, 0 vector (i.e. y-up or vector3.up)
    glScalef(0.5, 0.5, 0.5)
    mesh.draw()
    glLoadIdentity()  # this clears out the model view matrix so that the next mesh drawn is at the origin
    mesh.draw()  # this mesh is at the origin/not effected by glTranslated, glRotated, or glScale
    glPopMatrix()


done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    display()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()