# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
from numpy import fft


def freqspace(shape):
    x, y = shape
    # For n odd, both f1 and f2 are [-n+1:2:n-1]/n.
    # For n even, both f1 and f2 are [-n:2:n-2]/n.
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
        v[:,j] = x

    return u, v


img = Image.open('images/Fig10.10(a).jpg').show()
img = np.array(img)

shape = img.shape[0]*2, img.shape[1]*2
I_bg = np.zeros(shape)
I_bg[0:img.shape[0],0:img.shape[1]] = img

G = fft.fft2(I_bg)
G = fft.fftshift(G)
# G = 20*np.log(np.abs(G))


x, y = G.shape
# if x % 2 == 0:

u, v = freqspace(G.shape)
# G (2400, 3200)
u = u * y / 2
# U (3200, 2400)
v = v * x / 2
# V (3200, 2400)
D = np.sqrt(u**2 + v**2)
# D (3200, 2400)
D0 = 30
H = np.zeros(G.shape)
# H[D <= D0] = 1 # filtro ideal com corte em 30.
H = 1./(1+(D/D0)**(2*2))

F = G * H
F = fft.fftshift(F)
F = np.real(fft.ifft2(F))
F = F[0:img.shape[0],0:img.shape[1]]
print(F.shape)
Image.fromarray(F).show()
# print(F)
# imshow(uint8(F))
# H = 1./(1+(D./D0).^(2*n));
#
#
# Image.fromarray(img).show()
