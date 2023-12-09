#its a google colab specific code

from PIL import Image, ImageDraw
from IPython.display import display #used in google colab

import random

def generate_unique_art(width, height, num_shapes):
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    for _ in range(num_shapes):
        shape_type = random.choice(['rectangle', 'ellipse'])
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        if shape_type == 'rectangle':
            draw.rectangle([x1, y1, x2, y2], fill=color)
        elif shape_type == 'ellipse':
            draw.ellipse([x1, y1, x2, y2], fill=color)

    return img

width = 800
height = 600
num_shapes = 100

artwork = generate_unique_art(width, height, num_shapes)

# Display the generated image
display(artwork)
