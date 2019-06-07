# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 09/05/19
"""

from PIL import Image
import numpy as np
from numpy import fft
import copy
import MyLib as ml

img = Image.open('images/lena.tif')
img = np.array(img)

I_bg = ml.extendImg(img)               # Criando a imagem estendida de tamanho (2M, 2N)

G = ml.fshift(I_bg)                    # Multiplicando por (-1)^(x+y)
G = fft.fft2(G)                        # Calcula a DFT

D0 = [10, 30, 60]                      # Lista de valores de D0 utilizados
N = [1, 20]                            # Lista de valores do N
images = []
titles = []

for n in N:
    for d in D0:
        H = ml.imgFilter(G, d, n, 'btw')                 # Criando filtro butterworth
        F = G * H                                        # Convolucao no dominio da frequencia
        F = np.real(fft.ifft2(F))                        # Pegando a parte real da dft inversa
        F = ml.fshift(F)                                 # Multiplicando por (-1)^(x+y)
        F = F[0:img.shape[0], 0:img.shape[1]]            # Pegando a parte superior esquerda
        images.append(copy.deepcopy(F))                  # Adiciona a imagem na lista para ser imprimida
        titles.append("N = {} / D0 = {}".format(n, d))   # Adicionando titulo a lista

ml.show_images(images, 2, titles)
