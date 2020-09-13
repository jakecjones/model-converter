import vertices
import normals
import faces
import texture
import binary

fileName = "./model2.obj"
newObject = ""

f = open(fileName);
for line in f:
    index1 = line[0]
    index2 = line[1]
    index3 = line[2]

    newObject = newObject + line

    if index1 == "v" and index2 == " ":
        vertices.log(line)

    if index1 == "v" and index2 == "n":
        normals.log(line)

    if index1 == "f" and index2 == " ":
        faces.log(line)

    if index1 == "v" and index2 == "t":
        texture.log(line)

        f = open("newObject.obj", "w");
        f.write(newObject)
        f.close()
        
binary.writeBinaryToString()