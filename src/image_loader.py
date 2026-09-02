from pathlib import Path
from PIL import Image

def load_images(folder_path):

    images= []

    image_files = list(Path(folder_path).glob("*"))

    for image_file in image_files:

        if image_file.suffix.lower()in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
            
            img = Image.open(image_file)

            images.append({
            "path":str(image_file),
            "image": img,
            "filename":image_file.name})

    return images