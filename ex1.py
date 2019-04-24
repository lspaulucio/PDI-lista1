from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys

# Python configuration
sys.setrecursionlimit(5000)


def conta(img, i, j):
    shape = img.shape

    # Testing indexes
    if(i < 0 or i > (shape[0] - 1) or j < 0 or j > (shape[1] - 1)):
        return 0

    # Recursion
    if(img[i][j] == 255):
        img[i][j] = 0
        return 1 + conta(img, i, j+1) + conta(img, i, j-1) + conta(img, i-1, j) + conta(img, i+1, j)
    else:
        return 0


def contaPalito(img):
    shape = img.shape

    lin = int(shape[0]/2)
    newImg = img
    i = 1
    for j in range(0, shape[1]):
        if(newImg[lin][j] == 255):
            # print(lin, j)
            tam = conta(newImg, lin, j)
            print("Tamanho palito " + str(i) + " = " + str(tam))
            i += 1


def calculaHistograma(img):
    shape = img.shape
    histograma = np.zeros(256)

    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            histograma[img[i][j]] += 1

    return histograma


def binarizaImg(img, threshold):
    newImg = img
    shape = img.shape
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            if (newImg[i][j] >= THRESHOLD):
                newImg[i][j] = 255
            else:
                newImg[i][j] = 0

    return newImg


img = Image.open('images/Fig8.02.jpg')
# # plt.figure()
# # plt.plot(img.histogram())
#
img = np.array(img)
# print(img)

histograma = calculaHistograma(img)

plt.figure(2)
plt.title("Histograma")
plt.plot(histograma)
plt.show()

THRESHOLD = 160
imgBin = binarizaImg(img, THRESHOLD)
im = Image.fromarray(imgBin)
im.show()
contaPalito(img)
