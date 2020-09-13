
gltfBinary = "gltf/model.bin"

def writeBinaryToString():
    with open(gltfBinary, "rb") as file:
        data = file.read(8)
        with open("out.txt", "w") as f:
            f.write(" ".join([str(ord(c)) for c in data]))
