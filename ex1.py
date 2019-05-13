# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys

import MyLib as ml

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


img = Image.open('images/Fig8.02.jpg')
# # plt.plot(img.histogram())
#
img = np.array(img)
# print(img)

histograma = ml.calculaHistograma(img)

plt.figure(2)
plt.title("Histograma")
plt.plot(histograma)
plt.show(block=False)


THRESHOLD = 160
imgBin = ml.binarizaImg(img, THRESHOLD)
im = Image.fromarray(imgBin)
im.show()
contaPalito(img)
