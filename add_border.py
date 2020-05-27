import numpy as np
import sys
from PIL import Image

def add_border(image: np.array) -> np.array:
    # first remove any rows or columns from the edges that are already
    # all wall
    if (image[-1] == 0).all():
        image = image[0: -1, :] 
        
    if (image[:, 0] == 0).all():
        image = image[:, 1:]

    if (image[:, -1] == 0).all():
        image = image[:, : -1]

    if (image[0] == 0).all():
        image = image[1:, :]

    return np.pad(image, pad_width=1, mode='constant', constant_values=0)

def add_entrance_exit(image: np.array) -> np.array:
    row_length = len(image[0]) 
        
    for column in range(row_length):
        if image[1, column] == 255:
            image[0, column] = 255
            break

    for column in range(row_length - 1, -1, -1):
        if image[-2, column] == 255:
            image[-1, column] = 255
            break

    return image

if __name__ == '__main__':
    file_name = sys.argv[-1]
    open_image = Image.open(file_name).convert(mode='L')

    maze_array = np.array(open_image)
    maze_array = add_border(maze_array)
    maze_array = add_entrance_exit(maze_array)

    image = Image.fromarray(maze_array)
    image.save('maze_processed.gif')

