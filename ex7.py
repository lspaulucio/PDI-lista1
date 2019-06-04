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

images = []
titles = []
img = Image.open('images/mit_noise_periodic.jpg')
img = np.array(img)
# Image.fromarray(img).show()
I_bg = ml.extendImg(img)

G = ml.fshift(I_bg)
G = fft.fft2(G)

fourier = 20*np.log(np.abs(G+1))

# plt.imshow(20*np.log(np.abs(G+1)), cmap='gray')# Image.fromarray(20*np.log(np.abs(G))).show()

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
# plt.imshow(255*H, cmap='gray', alpha=0.3)
# plt.show()
# Image.fromarray(255*H).show()
filter = 255*H
# plt.imshow(255*H, cmap='gray', alpha=0.3)
# plt.show()
F = G * H

F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]

# Image.fromarray(F).show()
fig = plt.figure(figsize=(20, 10))
fig.add_subplot(221)
plt.title("Resultado após aplicar o Filtro")
plt.axis('off')
plt.imshow(F, cmap='gray')

histograma1 = ml.calculaHistograma(F)

fig.add_subplot(222)
plt.title("Histograma da Imagem")
plt.bar(histograma1[0], histograma1[1])

F2 = ml.equalizaHistograma(F)
histograma2 = ml.calculaHistograma(F2)

fig.add_subplot(223)
plt.title("Imagem com Histograma Equalizado")
plt.axis('off')
plt.imshow(F2, cmap='gray')

fig.add_subplot(224)
plt.title("Histograma Equalizado")
plt.bar(histograma2[0], histograma2[1])


images = [img, fourier, filter]
titles.append("Imagem Original")
titles.append("Espectro de Fourier da Imagem")
titles.append("Filtro utilizado")
ml.show_images(images, 1, titles)
