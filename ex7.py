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


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))


cid = fig.canvas.mpl_connect('button_press_event', onclick)

xc, yc = G.shape

D0 = 50
D = ml.frequenceSpace(G, (xc/2, yc/2))
H = ml.imgFilter(G, D, D0, 1, 'btw')
H = 1 - H

# print(H)
plt.imshow(255*H, cmap='gray', alpha=0.3)
plt.show()
# Image.fromarray(255*h).show()
F = G * H

F = np.real(fft.ifft2(F))
F = ml.fshift(F)
F = F[0:img.shape[0], 0:img.shape[1]]

Image.fromarray(F).show()


pares = []
pares.append((55,  700))
pares.append((55,  1350))
pares.append((145, 700))
pares.append((140, 1350))
pares.append((246, 695))
pares.append((332, 700))
pares.append((335, 1350))
pares.append((420, 1025))
pares.append((530, 700))
pares.append((530, 1355))
pares.append((1020, 700))
pares.append((1020, 1355))
pares.append((1020, 1027))
pares.append((1120, 1350))
pares.append((1200, 700))
pares.append((1200, 1350))
pares.append((1290, 700))
pares.append((1300, 1350))
pares.append((1400, 1350))
pares.append((1400, 700))
pares.append((1485, 700))
pares.append((1485, 1350))
