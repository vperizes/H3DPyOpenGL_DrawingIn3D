from OpenGL.GL import *
import pygame


class Rotation:
    def __init__(self, angle, axis):
        self.angle = angle
        self.axis = axis


class Mesh:
    # will store a translation vector. Translations need to happen before we draw anything
    def __init__(self, vertices, triangles, draw_type, translation, rotation, scale):  # these values will be passed through LoadMesh
        # and Cube (children of mesh)
        self.vertices = vertices
        self.triangles = triangles
        self.draw_type = draw_type
        self.translation = translation
        self.rotation = rotation
        self. scale = scale

    # Method for drawing
    def draw(self, move_to=pygame.Vector3(0, 0, 0)):
        glPushMatrix()  # using push/pop to make sure translation does not affect anything else being drawn
        glTranslatef(move_to.x, move_to.y, move_to.z)
        glTranslatef(self.translation.x, self.translation.y, self.translation.z)
        glScalef(self.scale.x, self.scale.y, self.scale.z)
        glRotatef(self.rotation.angle, self.rotation.axis.x, self.rotation.axis.y, self.rotation.axis.z)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        glPopMatrix()
