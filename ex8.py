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


def adaptativeMedian(img, Smax):
    window_size = 3  # window initial size
    padding_size = ml.getPaddingSize(img.shape, Smax)
    paddedImg = ml.paddingImage(img, padding_size, 'repeat')
    newImg = np.zeros(img.shape)
    for i in range(padding_size, newImg.shape[0]-padding_size):
        for j in range(padding_size, newImg.shape[1]-padding_size):
            temp_size = window_size
            stepA = True
            value = 0
            while(stepA):
                s = temp_size // 2
                window = paddedImg[i-s:i+s+1, j-s:j+s+1]
                # print(temp_size)
                # print(i,j,s)
                # print(window)
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
                    temp_size += 2               # senao aumente sxy
                    # print(temp_size)
                    if temp_size <= Smax[0]:  # se window_size <= smax repita A
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
imgT = adaptativeMedian(img, (17, 17))
# imgT = ml.medianFilter(img, kernel_shape=(7, 7))

# img_laplace = ml.conv2D(img, ml.MEAN_FILTER3, padding=5)  # padding 5 para manter o msm tamanho da imagem original
# # img_lowfilter = ml.conv2D(img, ml.MEAN_FILTER)
# print(ml.PSNR(imgOld, img_laplace))
# Image.fromarray(img_laplace).show(title="Laplaciano")
Image.fromarray(imgT).show(title="Laplaciano")

# Image.fromarray(img_lowfilter).show(title="Filtro passa baixo (média)")
