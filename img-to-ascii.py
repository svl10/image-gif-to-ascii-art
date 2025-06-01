import os
import sys
import time
import imageio
import numpy as np
from PIL import Image

# Dark - > Light
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Map pixels to ASCII characters
def pixel_to_ascii(pixel_value):
    return ASCII_CHARS[int(pixel_value / 25)]  # Scaling down pixel values

# Convert image to grayscale
def grayscale(image_path):
    img = Image.open(image_path)
    grayscale_image = img.convert("L")  # Convert to grayscale
    return grayscale_image

# Resize image
def resize_image(image, new_width=50):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Image into ASCII
def image_to_ascii(image_path, new_width=50):
    try:
        image = grayscale(image_path)
        image = resize_image(image, new_width)
        
        # Convert image to ASCII
        ascii_str = ""
        for y in range(image.height):
            for x in range(image.width):
                pixel_value = image.getpixel((x, y))
                ascii_str += pixel_to_ascii(pixel_value)
            ascii_str += "\n"
        
        return ascii_str
    except Exception as e:
        print(f"Error: {e}")
        return None

# Convert GIF to ASCII animation
def gif_to_ascii(gif_path, new_width=50, delay=0.1):
    try:
        gif = imageio.mimread(gif_path)
        while True:
            for frame in gif:
                img = Image.fromarray(frame)
                img = img.convert("L")
                img = resize_image(img, new_width)
                ascii_str = ""
                
                # Convert frame to ASCII
                for y in range(img.height):
                    for x in range(img.width):
                        pixel_value = img.getpixel((x, y))
                        ascii_str += pixel_to_ascii(pixel_value)
                    ascii_str += "\n"
                
                # Clear screen and print the frame
                os.system('cls' if os.name == 'nt' else 'clear')
                print(ascii_str)
                time.sleep(delay)
    except Exception as e:
        print(f"Error: {e}")
        return None

# Display an image or GIF as ASCII in the terminal
def display_ascii_art(image_path, is_gif=False, new_width=50, is_animated=False):
    if is_gif or image_path.endswith('.gif'):
        if is_animated:
            gif_to_ascii(image_path, new_width)
        else:
            print("Static GIF not supported yet for ASCII output.")
    else:
        ascii_str = image_to_ascii(image_path, new_width)
        if ascii_str:
            print(ascii_str)




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ascii_art.py <image_path> [--gif] [--animated] [--width <new_width>]")
        sys.exit(1)

    image_path = sys.argv[1]
    is_gif = '--gif' in sys.argv
    is_animated = '--animated' in sys.argv
    new_width = 50  # Default width

    if '--width' in sys.argv:
        width_index = sys.argv.index('--width') + 1
        if width_index < len(sys.argv):
            try:
                new_width = int(sys.argv[width_index])
            except ValueError:
                print("Invalid width, defaulting to 100.")
    
    display_ascii_art(image_path, is_gif, new_width, is_animated)
