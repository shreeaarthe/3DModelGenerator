import argparse
from utils.text_to_3d import generate_3d_from_text
from utils.image_to_3d import generate_3d_from_image
from utils.visualize import show_3d_model

parser = argparse.ArgumentParser()
parser.add_argument("--text", type=str, help="Text prompt like 'a small toy car'")
parser.add_argument("--image", type=str, help="Path to input image")
args = parser.parse_args()

if args.text:
    model_path = generate_3d_from_text(args.text)
elif args.image:
    model_path = generate_3d_from_image(args.image)
else:
    raise ValueError("Provide either --text or --image input.")

show_3d_model(model_path)
print(f"3D model saved at: {model_path}")
