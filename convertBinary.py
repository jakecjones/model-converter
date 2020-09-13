from pygltflib import GLTF2, BufferFormat

gltf = GLTF2().load("gltf/model.gltf")
gltf.convert_buffers(BufferFormat.DATAURI)  # convert buffer URIs to data.
gltf.save("test.gltf") 