# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

import MyLib as ml

img = Image.open('images/lena.tif')
img = np.array(img)

I_bg = ml.extendImg(img)

G = ml.fshift(I_bg)
G = fft.fft2(G)
# Image.fromarray(20*np.log(np.abs(G))).show()

D0 = 30
H = ml.imgFilter(G, D0, 1, 'btw')
Image.fromarray(255*H).show()

F = G * H
# Image.fromarray(20*np.log(np.abs(F))).show()

F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]
Image.fromarray(F).show()
plt.imshow(F, cmap='gray')
plt.axis('off')
plt.show()
