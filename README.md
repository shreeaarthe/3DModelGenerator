Steps to Run: 

First, set up a virtual environment and activate it (basically create a clean workspace for your project).
Then, install all the necessary libraries by running pip install -r requirements.txt.
Now, you can run the program by providing either an image or a text prompt:
For an image: python app.py --image chair.jpg
For a text prompt: python app.py --text "a small toy car"
The program will process the input, generate a 3D model, save it as a .obj file, and open a 3D viewer so you can see your model!

Libraries Used: 

rembg: Used to remove the background from images, so only the object is kept.
trimesh: Helps create and export 3D models in the .obj format.
pyrender: Allows me to display the 3D models interactively in a viewer.
imageio: For loading and working with image files.
argparse: Makes it easy to handle command-line inputs.

Code Structure:

3DModelGenerator/

├── app.py                  # Main execution file

├── utils/

│   ├── image_to_3d.py      # Converts image to 3D model

│   ├── text_to_3d.py       # Converts text to 3D model

│   └── visualize.py        # Shows 3D viewer

├── output/                 # Stores generated 3D files

├── requirements.txt        # Python dependencies

└── README.md

Thought Process:

The goal was to build a simple tool that can turn either a picture or a text description into a 3D model. For the images, I used AI to remove the background and focus only on the object. 
For text, I just used a basic placeholder model (a cube) for now. I used trimesh to create the 3D objects and pyrender to display them. The code is clean and modular, so I can easily replace 
the placeholders with more realistic AI-generated models later on.

Video demo - https://drive.google.com/file/d/1bDcySS-pjhIBMc1tisMXyMJbFgZRTXNA/view?usp=sharing

Thank you!

