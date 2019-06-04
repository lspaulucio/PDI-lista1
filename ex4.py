# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
from numpy import fft
import copy
import MyLib as ml

img = Image.open('images/lena.tif')
img = np.array(img)

I_bg = ml.extendImg(img)

G = ml.fshift(I_bg)
G = fft.fft2(G)
# Image.fromarray(20*np.log(np.abs(G))).show()

D0 = [10, 30, 60]
N = [1, 20]
images = []
titles = []

for n in N:
    for d in D0:
        H = ml.imgFilter(G, d, n, 'btw')
        # Image.fromarray(255*H).show()
        F = G * H
        # Image.fromarray(20*np.log(np.abs(F))).show()
        F = np.real(fft.ifft2(F))
        F = ml.fshift(F)
        F = F[0:img.shape[0], 0:img.shape[1]]
        images.append(copy.deepcopy(F))
        titles.append("N = {} / D0 = {}".format(n, d))

ml.show_images(images, 2, titles)
