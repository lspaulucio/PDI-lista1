# -*- coding: utf-8 -*-
import numpy as np

def calculaHistograma(img):
    shape = img.shape
    histograma = np.zeros(256)
    x = [i for i in range(0, 256)]
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            histograma[int(img[i][j])] += 1

    return x, histograma


def binarizaImg(img, threshold):
    newImg = img
    shape = img.shape
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            if (newImg[i][j] > threshold):
                newImg[i][j] = 255
            else:
                newImg[i][j] = 0

    return newImg


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
        paddedImg = np.full(shape, 255)

    paddedImg[padding:-padding, padding:-padding] = img
    newImg = np.zeros((getOutputSize(img.shape, kernel.shape, padding, stride)))
    x = kernel.shape[0]
    y = kernel.shape[1]
    for i in range(0, newImg.shape[0]):
        for j in range(0, newImg.shape[1]):
            value = (kernel * paddedImg[i:i+y, j:j+x]).sum()
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            newImg[i][j] = value

    return newImg


def medianFilter(img, kernel_shape=(3, 3)):
    newImg = np.zeros(img.shape)
    x = kernel_shape[0]
    y = kernel_shape[1]
    for i in range(0, newImg.shape[0]):
        for j in range(0, newImg.shape[1]):
            value = np.median(img[i:i+y, j:j+x])
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            newImg[i][j] = value

    return newImg


# ############################# Filters ################################

MEAN_FILTER = np.ones((3, 3)) / 9.0

MEAN_FILTER2 = 1/16. * np.array([[1, 2, 1],
                                 [2, 4, 2],
                                 [1, 2, 1]])

LAPLACE_FILTER = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])

SOBEL_FILTER = np.array([[1,   2,  1],
                         [0,   0,  0],
                         [-1, -2, -1]])


# ############################ Frequence domain functions

def frequenceSpace(img, center):
    D = np.zeros(img.shape)
    for u in range(0, img.shape[0]):
        for v in range(0, img.shape[1]):
            D[u][v] = np.sqrt((u - center[0])**2 + (v - center[1])**2)
    return D


def fshift(img):
    for u in range(0, img.shape[0]):
        for v in range(0, img.shape[1]):
            img[u][v] *= (-1)**(u+v)
    return img


def extendImg(img):
    newShape = img.shape[0]*2, img.shape[1]*2
    I_bg = np.zeros(newShape)
    I_bg[0:img.shape[0], 0:img.shape[1]] = img
    return I_bg


def imgFilter(img, D, D0=30, n=1, filterType='btw'):
    H = np.zeros(img.shape)
    H = 1./(1+(D/D0)**(2*n))
    return H


def notchFilter(img, D0, n, filterType='btw', center=None):
    if center is None:
        center = img.shape
    D = np.zeros(img.shape)
    for u in range(0, img.shape[0]):
        for v in range(0, img.shape[1]):
            for y, x in center:
                D = np.sqrt((u - x)**2 + (v - y)**2)
    return D


def freqspace(shape):
    x, y = shape
    # For n even, both f1 and f2 are [-n:2:n-2]/n.
    # For n odd, both f1 and f2 are [-n+1:2:n-1]/n.
    if x % 2 == 0:
        x = [i/x for i in range(-x, x-2+1, 2)]
    else:
        x = [i/x for i in range(-x+1, x-1+1, 2)]

    if y % 2 == 0:
        y = [i/y for i in range(-y, y-2+1, 2)]
    else:
        y = [i/y for i in range(-y+1, y-1+1, 2)]

    rows, cols = len(x), len(y)

    u = np.zeros((rows, cols))
    v = np.zeros((rows, cols))

    for i in range(0, rows):
        u[i] = y
    for j in range(0, cols):
        v[:, j] = x

    return u, v
