import pygame
from OpenGL.GLU import *
from math import *


class Camera:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 0)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward

    def update_camera(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward
        elif keys[pygame.K_UP]:
            self.eye += self.forward
        elif keys[pygame.K_RIGHT]:
            self.eye -= self.right
        elif keys[pygame.K_LEFT]:
            self.eye += self.right

        self.look = self.eye + self.forward  # need to update self.look since eye has moved
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)
