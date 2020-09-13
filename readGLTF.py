
import pathlib
import struct

import miniball
import numpy
from pygltflib import GLTF2

def writeBinaryToString():
    fname = "gltf/box.gltf"
    gltf = GLTF2().load(fname)
    # get the first mesh in the current scene (in this example there is only one scene and one mesh)
    mesh = gltf.meshes[gltf.scenes[gltf.scene].nodes[0]]

    # get the vertices for each primitive in the mesh (in this example there is only one)
    for primitive in mesh.primitives:
        # get the binary data for this mesh primitive from the buffer
        accessor = gltf.accessors[primitive.attributes.POSITION]
        bufferView = gltf.bufferViews[accessor.bufferView]
        buffer = gltf.buffers[bufferView.buffer]
        data = gltf.decode_data_uri(buffer.uri)

        # pull each vertex from the binary buffer and convert it into a tuple of python floats
        vertices = []
        for i in range(accessor.count):
            index = bufferView.byteOffset + accessor.byteOffset + i*12  # the location in the buffer of this vertex
            d = data[index:index+12]  # the vertex data
            v = struct.unpack("<fff", d)   # convert from base64 to three floats
            vertices.append(v)
            print(i, v)

    # convert a numpy array for some manipulation
    S = numpy.array(vertices)

    # use a third party library to perform Ritter's algorithm for finding smallest bounding sphere
    C, radius_squared = miniball.get_bounding_ball(S)

    # output the results
    print(f"center of bounding sphere: {C}\nradius squared of bounding sphere: {radius_squared}")