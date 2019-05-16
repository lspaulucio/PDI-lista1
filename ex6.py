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

img = Image.open('images/camisa.jpg')
img = np.array(img)
# Image.fromarray(img).show()
I_bg = ml.extendImg(img)

G = ml.fshift(I_bg)
G = fft.fft2(G)
# Image.fromarray(20*np.log(np.abs(G))).show()
plt.imshow(20*np.log(np.abs(G)), cmap='gray')
U, V = G.shape

D0 = 150
# 2400 3200
# H = ml.notchFilter(G, D0, 5, center=(205, 381)) * \
#     ml.notchFilter(G, D0, 5, center=(V-205, U-381))
H = ml.imgFilter(G, 100, 2)
plt.imshow(255*H, cmap='gray', alpha=0.3)
plt.show()
# xdata=205.262987, ydata=381.805195
# Image.fromarray(255*H).show()
F = G * H
plt.imshow(20*np.log(np.abs(F)), cmap='gray')
plt.show()
F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]

Image.fromarray(F).show()
