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

images = []
titles = []

img = Image.open('images/camisa.jpg')
img = np.array(img)
images.append(img)
# Image.fromarray(img).show()
I_bg = ml.extendImg(img)
G = ml.fshift(I_bg)
G = fft.fft2(G)
# Image.fromarray(20*np.log(np.abs(G+1))).show()
images.append(20*np.log(np.abs(G+1)))
# plt.imshow(20*np.log(np.abs(G)), cmap='gray')
U, V = G.shape

D0 = 150
H = ml.notchFilter(G, D0, 5, center=(205, 381)) * \
    ml.notchFilter(G, D0, 5, center=(V-205, U-381))
# H = ml.imgFilter(G, 100, 2)
# plt.imshow(255*H, cmap='gray', alpha=0.3)
# plt.show()
# Image.fromarray(255*H).show()
images.append(255*H)
F = G * H
F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]
# Image.fromarray(F).show()
images.append(copy.deepcopy(F))

H = ml.imgFilter(G, 100, 2)
# plt.imshow(255*H, cmap='gray', alpha=0.3)
# plt.show()
images.append(255*H)
F = G * H
F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]
# Image.fromarray(F).show()
images.append(copy.deepcopy(F))
sortimages = [images[0], images[2], images[4], images[1], images[3], images[5]]
titles = ["Imagem Original", "Filtro Notch", "Filtro Passa Baixa Butterworth", "FFT da Imagem Original",
          "Resultado com Filtro Notch", "Resultado com Filtro Butterworth"]
ml.show_images(sortimages, 2, titles)
