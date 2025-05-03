import trimesh
import pyrender

def show_3d_model(file_path):
    mesh = trimesh.load(file_path)
    scene = pyrender.Scene()
    render_mesh = pyrender.Mesh.from_trimesh(mesh)
    scene.add(render_mesh)

    pyrender.Viewer(scene, use_raymond_lighting=True)
