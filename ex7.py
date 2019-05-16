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

img = Image.open('images/mit_noise_periodic.jpg')
img = np.array(img)
Image.fromarray(img).show()
I_bg = ml.extendImg(img)

G = ml.fshift(I_bg)
G = fft.fft2(G)
# Image.fromarray(20*np.log(np.abs(G))).show()

fig = plt.figure()

plt.imshow(20*np.log(np.abs(G)), cmap='gray')
plt.axis("off")

U, V = G.shape

D0 = 50
N = 5
H = ml.notchFilter(G, D0, N, center=(1030, 422)) * \
    ml.notchFilter(G, D0, N, center=(700, 525)) * \
    ml.notchFilter(G, D0, N, center=(560, 765)) * \
    ml.notchFilter(G, D0, N, center=(700, 525)) * \
    ml.notchFilter(G, D0, N, center=(695, 1000)) * \
    ml.notchFilter(G, D0, N, center=(V - 700, U - 525)) * \
    ml.notchFilter(G, D0, N, center=(V - 560, U - 765)) * \
    ml.notchFilter(G, D0, N, center=(V - 700, U - 525)) * \
    ml.notchFilter(G, D0, N, center=(V - 695, U - 1000)) * \
    ml.notchFilter(G, D0, N, center=(V - 1030, U - 422))

# print(H)
# plt.imshow(255*H, cmap='gray', alpha=0.3)
# plt.show()
# Image.fromarray(255*H).show()
plt.imshow(255*H, cmap='gray', alpha=0.3)
plt.show()
F = G * H

F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]

Image.fromarray(F).show()

F = ml.equalizaHistograma(F)
Image.fromarray(F).show()
