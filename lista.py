from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

kernel = np.array([[-1, -2, -1],
                   [0,   0,  0],
                   [1,   2,  1]])

kernel2 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

# print(kernel*kernel2)


def getSubImg(img, i, j):

    np.array([[img[i-1][j-1], img[i-1][j], img[i-1][j+1]],
              [img[i][j-1],   img[i][j],   img[i][j+1]],
              [img[i+1][j-1], img[i+1][j], img[i+1][j+1]]])


def getOutputSize(old_shape,kernel_shape, padding, stride):
    return int((old_shape + 2*padding - kernel_shape)/stride + 1)

def getNewSize(shape, padding):
    return int((shape + 2*padding))


def conv2D(img, kernel, stride=1, padding=1, padding_value=0):
    shape = []
    newImg = []
    for i in range(0, 2):
        size = getNewSize(img.shape[i], padding)
        shape.append(size)

    kernel = np.flip(kernel)

    if padding_value == 0:
        newImg = np.zeros((shape))
    elif padding_value == 1:
        newImg = np.ones((shape))

    newImg[padding:-padding, padding:-padding] = img

    



img = Image.open('images/lena.tif')
img.show()
img = np.array(img)
# print(img.shape)
conv2D(img, kernel, padding=1)
