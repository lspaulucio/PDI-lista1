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

plt.imshow(np.log(np.abs(G)), cmap='gray')
plt.axis("off")
# plt.show()
U, V = G.shape

D0 = 50
N = 20
H = np.zeros(G.shape)
# H = ml.notchFilter(G, D0, N, center=(1025, 425)) * \
#     ml.notchFilter(G, D0, N, center=(700, 525)) * \
#     ml.notchFilter(G, D0, N, center=(560, 765)) * \
#     ml.notchFilter(G, D0, N, center=(695, 1000)) * \
#     ml.notchFilter(G, D0, N, center=(V - 560, U - 765)) * \
#     ml.notchFilter(G, D0, N, center=(V - 700, U - 525)) * \
#     ml.notchFilter(G, D0, N, center=(V - 695, U - 1000)) * \
#     ml.notchFilter(G, D0, N, center=(V - 1025, U - 425)) * \
#     ml.notchFilter(G, 6, N, type='ideal', center=(1033, 755)) * \
#     ml.notchFilter(G, 6, N, type='ideal', center=(V - 1033, U - 755))

SIZE = 10
H[:, 700-SIZE:700+SIZE] = 1
H[:, 562-SIZE:562+SIZE] = 1
H[:, 1350-SIZE:1350+SIZE] = 1
H[:, 1483-SIZE:1483+SIZE] = 1
H[1010-SIZE:1010+SIZE, :] = 1
H[1112-SIZE:1112+SIZE, :] = 1
H[420-SIZE:420+SIZE, :] = 1
H[523-SIZE:523+SIZE, :] = 1
H[768-SIZE:768+SIZE, 0:700] = 1
H[768-SIZE:768+SIZE, 1350:2047] = 1
H[:523, 1024-SIZE:1024+SIZE] = 1
H[1010:, 1024-SIZE:1024+SIZE] = 1
H[756-7:756+7, 1033-5:1033+5] = 1
H[780-7:780+7, 1015-5:1015+5] = 1
H = 1 - H
# 1115 780
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
F = ml.medianFilter(F, kernel_shape=(3, 3))
F = ml.equalizaHistograma(F)
Image.fromarray(F).show()
