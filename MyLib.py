# -*- coding: utf-8 -*-
import numpy as np


def D(img):
    D = np.zeros(img.shape)
    for u in range(0, img.shape[0]):
        for v in range(0, img.shape[1]):
            D[u][v] = np.sqrt((u - img.shape[0]/2)**2 + (v - img.shape[1]/2)**2)
    return D


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
