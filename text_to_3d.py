import os
import trimesh

def generate_3d_from_text(prompt):
    print(f"Generating 3D model for text: {prompt}")
    
    os.makedirs("output", exist_ok=True)
    output_file = "output/text_model.obj"

    # Placeholder: Box for demonstration
    mesh = trimesh.primitives.Box(extents=(1, 0.5, 0.3))
    mesh.export(output_file)

    return output_file
