# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
from numpy import fft


def freqspace(shape):
    x, y = shape
    # For n even, both f1 and f2 are [-n:2:n-2]/n.
    # For n odd, both f1 and f2 are [-n+1:2:n-1]/n.
    if x % 2 == 0:
        x = [i/x for i in range(-x, x-2+1, 2)]
    else:
        x = [i/x for i in range(-x+1, x-1+1, 2)]

    if y % 2 == 0:
        y = [i/y for i in range(-y, y-2+1, 2)]
    else:
        y = [i/y for i in range(-y+1, y-1+1, 2)]

    rows, cols = len(x), len(y)

    u = np.zeros((rows, cols))
    v = np.zeros((rows, cols))

    for i in range(0, rows):
        u[i] = y
    for j in range(0, cols):
        v[:, j] = x

    return u, v


img = Image.open('images/mit_noise_periodic.jpg')
img = np.array(img)
# Image.fromarray(img).show()
shape = img.shape[0]*2, img.shape[1]*2
I_bg = np.zeros(shape)
I_bg[0:img.shape[0], 0:img.shape[1]] = img

G = fft.fft2(I_bg)
G = fft.fftshift(G)
G = 20*np.log(np.abs(G))
Image.fromarray(G).show()

x, y = G.shape
# # if x % 2 == 0:
u, v = freqspace(G.shape)
# # G (2400, 3200)
u = u * y / 2
v = v * x / 2
D = np.sqrt(u**2 + v**2)
# # D (3200, 2400)
D0 = 20
H = np.zeros(G.shape)
# H[D <= D0] = 1 # filtro ideal com corte em 30.
H = 1./(1+(D/D0)**(2*1))
#
F = G * H
F = fft.ifftshift(F)
F = np.real(fft.ifft2(F))
F = F[0:img.shape[0], 0:img.shape[1]]

# # print(F.shape)
# Image.fromarray(F).show()
# # imshow(uint8(F))
# # H = 1./(1+(D./D0).^(2*n));
# #
# #
# # Image.fromarray(img).show()
