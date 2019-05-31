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
    window_size = (3, 3)

    # zmin valor minimo de intensidade na janela
    # zmax valor maximo de intensidade na janela
    # zmed mediana de intensidade na janela
    # zxy valor do pixel
    # smax valor maximo da janela

    # zmed = mediana dos valores de intensidade em Sxy
    # stepA
    # a1 = zmed -zmin
    # a2 = zmed - zmax
    # se a1 > 0 e a2 < 0 goto B
    # senao aumente sxy
    # se window_size <= smax repita A
    # senao saida é zmed

    # stepB
    # b1 = zxy - zmin
    # b2 = zxy -zmax
    # se b1 > 0 e b2 <0 saida é zxy
    # senao a saida é zmed

    print(window_size)




img = Image.open('images/ruidosa2.tif')
img = np.array(img)
imgOld = copy.deepcopy(img)
img_laplace = ml.conv2D(img, ml.MEAN_FILTER3, padding=5)  # padding 5 para manter o msm tamanho da imagem original
# img_lowfilter = ml.conv2D(img, ml.MEAN_FILTER)
print(ml.PSNR(imgOld, img_laplace))
Image.fromarray(img_laplace).show(title="Laplaciano")

# Image.fromarray(img_lowfilter).show(title="Filtro passa baixo (média)")
