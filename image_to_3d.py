from rembg import remove
from PIL import Image
import trimesh
import os

def generate_3d_from_image(image_path):
    print(f"Processing image: {image_path}")
    
    os.makedirs("output", exist_ok=True)
    output_path = "output/image_model.obj"

    # Remove background
    image = Image.open(image_path)
    result = remove(image)
    result.save("output/cleaned.png")

    # Placeholder box model
    mesh = trimesh.primitives.Box(extents=(0.6, 0.6, 0.6))
    mesh.export(output_path)

    return output_path
