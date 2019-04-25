from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

kernel = np.array([[1.0/9.0, 1.0/9.0, 1.0/9.0],
                   [1.0/9.0, 1.0/9.0, 1.0/9.0],
                   [1.0/9.0, 1.0/9.0, 1.0/9.0]])

laplace = np.array([[-1, -1, -1],
                    [-1,  9, -1],
                    [-1, -1, -1]])

# print(kernel*kernel2)


def getSubImg(img, i, j):

    np.array([[img[i-1][j-1], img[i-1][j], img[i-1][j+1]],
              [img[i][j-1],   img[i][j],   img[i][j+1]],
              [img[i+1][j-1], img[i+1][j], img[i+1][j+1]]])


def getOutputSize(old_shape, kernel_shape, padding, stride):
    return int((old_shape[0] + 2*padding - kernel_shape[0])/stride + 1), \
           int((old_shape[1] + 2*padding - kernel_shape[1])/stride + 1)


def getNewSize(shape, padding):
    return int((shape + 2*padding))


def conv2D(img, kernel, stride=1, padding=1, padding_value=0):
    shape = []
    paddedImg = []
    newImg = []
    for i in range(0, 2):
        size = getNewSize(img.shape[i], padding)
        shape.append(size)

    kernel = np.flip(kernel)

    if padding_value == 0:
        paddedImg = np.zeros((shape))
    elif padding_value == 1:
        paddedImg = np.ones((shape))

    paddedImg[padding:-padding, padding:-padding] = img
    newImg = np.zeros((getOutputSize(img.shape, kernel.shape, padding, stride)))
    print(newImg.shape)
    x = kernel.shape[0]
    y = kernel.shape[1]
    print(kernel.shape)
    for i in range(0, newImg.shape[0]):
        for j in range(0, newImg.shape[1]):
            newImg[i][j] = (kernel * paddedImg[i:(i+y), j:(j+x)]).sum()

    return newImg


img = Image.open('images/lena.tif')
# img.show()
img = np.array(img)
print(img.shape)
img = conv2D(img, kernel, padding=1)
Image.fromarray(img).show()
