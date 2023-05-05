from OpenGL.GL import *
from Mesh import *


# Load mesh inherits properties from mesh
class LoadMesh(Mesh):
    def __init__(self, filename, draw_type, position=pygame.Vector3(0, 0, 0)):  # passing a default position at origin
        self.filename = filename
        vertices, triangles = self.load_drawing()  # returning vertices & triangles from load_drawing then passing to super
        super().__init__(vertices, triangles, draw_type, position)

    def load_drawing(self):
        vertices = []  # now local to method
        triangles = []  # now local to method
        with open(self.filename) as fp:
            line = fp.readline()  # reading through file one line at a time
            while line:
                # this if statement get the vertices from obj file
                if line[:2] == "v ":  # checking substring from the line that is 2 characters long
                    vx, vy, vz = [float(value) for value in line[2:].split()]  # this get the vertex values starting at
                    # substring index 2 onward, splits them at the space between the values, and assigns each split
                    # value to vx, vy, vz
                    vertices.append((vx, vy, vz))

                # this if statement gets triangle vertices from the face data. Faces are made up of three different
                # triangle sets. For this exercise, we only want the first triangle value in each set
                if line[:2] == "f ":
                    # first separating the strings of triangle vertices. For example t1 = 1/1/1, t2 = 2/2/1
                    # (note: focus on data structure not numbers)
                    t1, t2, t3 = [value for value in line[2:].split()]
                    # here we are extracting the first element in the string of three vertices and appending it to the
                    # triangles array. In the obj file 1st vertex is assigned to the number 1 but in our array 0 is the
                    # first position we must subtract by 1 so vertices are stored in the correct position in
                    # the triangles array
                    triangles.append([int(value) for value in t1.split('/')][0]-1)
                    triangles.append([int(value) for value in t2.split('/')][0]-1)
                    triangles.append([int(value) for value in t3.split('/')][0]-1)
                line = fp.readline()  # prevents from reading the same line, allows to exit while loop
        return vertices, triangles

