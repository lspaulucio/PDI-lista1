# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
import MyLib as ml
import copy


def paddingImage(img, padding_size=1):
    shape = img.shape
    shape = (shape[0]+2*padding_size, shape[1]+2*padding_size)
    new = np.zeros(shape)
    new[padding_size:-padding_size, padding_size:-padding_size] = img
    return new


# zmin valor minimo de intensidade na janela
# zmax valor maximo de intensidade na janela
# zmed mediana de intensidade na janela
# zxy valor do pixel
# smax valor maximo da janela
def adaptativeMedian(img, Smax):
    window_size = np.array([3, 3])  # window initial size
    padding_size = ml.getPaddingSize(img.shape, Smax)
    paddedImg = paddingImage(img, padding_size)
    newImg = np.zeros(img.shape)
    for i in range(padding_size, newImg.shape[0]):
        for j in range(padding_size, newImg.shape[1]):
            temp_size = window_size
            stepA = True
            value = 0
            while(stepA):
                x, y = temp_size[0] // 2, temp_size[1] // 2
                window = paddedImg[i-y:i+y+1, j-x:j+x+1]
                print(window)
                zmed = np.median(window)
                zmin = np.min(window)
                zmax = np.max(window)
                zxy = paddedImg[i, j]
                # StepA
                a1 = zmed - zmin                 # a1 = zmed -zmin
                a2 = zmed - zmax                 # a2 = zmed - zmax
                if a1 > 0 and a2 < 0:            # se a1 > 0 e a2 <0 goto step B
                    # stepB
                    b1 = zxy - zmin              # b1 = zxy - zmin
                    b2 = zxy - zmax              # b2 = zxy - zmax
                    if b1 > 0 and b2 < 0:        # se b1 > 0 e b2 < 0
                        value = zxy              # saida e zxy
                        stepA = False
                    else:
                        value = zmed             # senao saida e zmed
                        stepA = False
                else:
                    # print(temp_size)
                    temp_size += 2*np.ones(2, dtype=np.int)    # senao aumente sxy
                    # print(temp_size)
                    if temp_size[0] <= Smax[0]:  # se window_size <= smax repita A
                        print(temp_size)
                        stepA = True
                    else:
                        value = zmed             # senao saida e zmed
                        stepA = False

            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            newImg[i][j] = value
        # print(i)

    return newImg


img = Image.open('images/ruidosa2.tif')
img = np.array(img)
imgOld = copy.deepcopy(img)
imgT = adaptativeMedian(img, (7, 7))
# img_laplace = ml.conv2D(img, ml.MEAN_FILTER3, padding=5)  # padding 5 para manter o msm tamanho da imagem original
# # img_lowfilter = ml.conv2D(img, ml.MEAN_FILTER)
# print(ml.PSNR(imgOld, img_laplace))
# Image.fromarray(img_laplace).show(title="Laplaciano")
Image.fromarray(imgT).show(title="Laplaciano")

# Image.fromarray(img_lowfilter).show(title="Filtro passa baixo (média)")
