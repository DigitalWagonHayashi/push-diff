import cv2
import os
import numpy as np
from numpy import uint8


def push_diff(img1_path: str, img2_path: str):
    img1 = cv2.imread(img1_path, -1)
    img2 = cv2.imread(img2_path, -1)
    print(type(img2))
    print(type(img2[0]))
    print(type(img2[0][0]))
    print(img2[0][0].dtype)
    diff_coordinate = []
    for height in range(len(img1)):
        diff_coordinate_tmp = []
        for width in range(len(img1[0])):
            if list(img1[height][width]) != list(img2[height][width]):
                diff_coordinate_tmp.append(img2[height][width])
            else:
                img2[height][width][3] = 0
                diff_coordinate_tmp.append(img2[height][width])
        diff_coordinate.append(diff_coordinate_tmp)
    print(diff_coordinate[0])
    cv2.imwrite(f'{img2_path}_diff_on_{os.path.basename(img1_path)}.png', np.array(diff_coordinate))


if __name__ == '__main__':
    push_diff()
    print()
