from PIL import Image
import random
import os

def create_random_images(n, h, w, folder_path):
    os.makedirs(folder_path, exist_ok=True)
    
    for i in range(n):
        image = Image.new('RGB', (w, h))
        pixels = []

        for _ in range(h):
            row = []
            for _ in range(w):
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                pixel = (red, green, blue)
                row.append(pixel)
            pixels.append(row)

        image.putdata([pixel for row in pixels for pixel in row])
        file_path = os.path.join(folder_path, f"image_{i+1}.png")
        image.save(file_path)
        print(f"Image {i+1} saved at {file_path}")

# Example usage
create_random_images(100, 128, 128, r"F:\TestImage\128")
create_random_images(100, 256, 256, r"F:\TestImage\256")
create_random_images(100, 384, 384, r"F:\TestImage\384")
create_random_images(100, 512, 512, r"F:\TestImage\512")
create_random_images(100, 640, 640, r"F:\TestImage\640")