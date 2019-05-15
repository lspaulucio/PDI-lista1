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

img = Image.open('images/camisa.jpg')
img = np.array(img)
# Image.fromarray(img).show()

I_bg = ml.extendImg(img)

G = ml.fshift(I_bg)
G = fft.fft2(G)
# Image.fromarray(20*np.log(np.abs(G))).show()

xc, yc = G.shape

D0 = 30
D = ml.frequenceSpace(G, (xc/2, yc/2))
H = ml.imgFilter(G, D, D0, 1, 'btw')
F = G * H

F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]

Image.fromarray(F).show()
