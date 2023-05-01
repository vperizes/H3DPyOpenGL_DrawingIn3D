from OpenGL.GL import *
from Mesh import *


class LoadMesh(Mesh):
    def __init__(self, filename, draw_type):
        self.vertices = []
        self.triangles = []
        self.filename = filename
        self.draw_type = draw_type
        self.load_drawing()  # running the loading method for loading in mesh from a given obj file

    def load_drawing(self):
        with open(self.filename) as fp:
            line = fp.readline()  # reading through file one line at a time
            while line:
                # this if statement get the vertices from obj file
                if line[:2] == "v ":  # checking substring from the line that is 2 characters long
                    vx, vy, vz = [float(value) for value in line[2:].split()]  # this get the vertex values starting at
                    # substring index 2 onward, splits them at the space between the values, and assigns each split
                    # value to vx, vy, vz
                    self.vertices.append((vx, vy, vz))

                # this if statement gets triangle vertices from the face data. Faces are made up of three different
                # triangle sets. For this exercise, we only want the first triangle value in each set
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]  # first separating the strings of triangle
                    # vertices. For example t1 = 1/1/1, t2 = 2/2/1 (note: focus on data structure not numbers)
                    self.triangles.append([int(value) for value in t1.split('/')][0]-1)  # here we are extracting the
                    # first element in the string of three vertices and appending it to the triangles array.
                    # in the obj file 1st vertex is assigned to the number 1 but in our array 0 is the first position
                    # we must subtract by 1 so vertices are stored in the correct position in the triangles array
                    self.triangles.append([int(value) for value in t2.split('/')][0]-1)
                    self.triangles.append([int(value) for value in t3.split('/')][0]-1)
                line = line = fp.readline()  # prevents from reading the same line, allows to exit while loop

