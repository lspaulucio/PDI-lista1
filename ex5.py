# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
from numpy import fft

import MyLib as ml

img = Image.open('images/mar-il.gif')
img = np.array(img)

I_bg = ml.extendImg(img)

G = ml.fshift(I_bg)
G = fft.fft2(G)
# Image.fromarray(G).show()

xc, yc = G.shape

D0 = 80
H = ml.filterHomomorphic(G, D0, yh=2, yl=0.25)
F = G * H
F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]
F = ml.equalizaHistograma(F)
# Image.fromarray(F).show()
images = [img, F]
ml.show_images(images)
