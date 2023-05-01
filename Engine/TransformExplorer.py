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
mesh = LoadMesh("teapot.obj", GL_LINE_LOOP)

eye = [0, 0, 0]  # initial camera positions that get updated

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 500.0)


def init_camera():
    # modelview
    glMatrixMode(GL_MODELVIEW)  # this switches open GL to model view mode. Any operations after this line are applied
    # to model view matrix
    glLoadIdentity()
    # glTranslated(0, 0, -2)  # camera is sitting at origin looking down neg z-axis (neg z goes into screen) - need to
    # push model back to make it visible. Default: pos x is to the right and pos y is up
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)  # we change the camera transform in the model view. gluLookAt uses the
    # following format (eye.x, eye.y, eye.z, look.x, look.y, look.z, up.x, up.y, up.z). 'eye' refers to the eye/camera
    # location. 'look' refers to the point the camera is looking at (here we look at the origin where the teapot
    # is). 'up' refers to the orientation of camera


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init_camera()
    glPushMatrix()
    mesh.draw()
    glPopMatrix()


done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        eye[2] += 1  # this moves the camera back in the pos z dir
    elif keys[pygame.K_UP]:
        eye[2] -= 1  # this moves camera up in the pos y dir
    display()
    pygame.display.flip()
    # pygame.time.wait(10)
pygame.quit()