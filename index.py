import vertices
import normals
import faces
import texture

fileName = "./model.obj"
f = open(fileName);
for line in f:
    index1 = line[0]
    index2 = line[1]
    index3 = line[2]
    if index1 == "v" and index2 == " ":
        vertices.log(line)
    if index1 == "v" and index2 == "n":
        normals.log(line)
    if index1 == "f" and index2 == " ":
        faces.log(line)
    if index1 == "v" and index2 == "t":
        texture.log(line)
