import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
new_folder = sys.argv[2]
# check if new/ exist, if not create
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

save_path = os.path.join(new_folder,)
# loop through Pokedex,
for item in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{item}')
    png_file = item.replace('.jpg', '.png')
    img.save(f'{new_folder}{png_file}')
# convert images to png
# save to the new folder.