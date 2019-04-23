from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

kernel = np.array([[-1, -2, -1],
                   [0,   0,  0],
                   [1,   2,  1]])

kernel2 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

print(kernel*kernel2)

# def conv2D(img, kernel):
# print(np.flip(kernel))

def getSubImg(img, i, j):

    np.array([[img[i-1][j-1], img[i-1][j], img[i-1][j+1]],
              [img[i][j-1],   img[i][j],   img[i][j+1]],
              [img[i+1][j-1], img[i+1][j], img[i+1][j+1]]])

for i in range(0, shape[0]):
    for j in range(0, shape[1]):
