from PIL import Image
import numpy as np
import scipy.fftpack as fp
import math

im2freq = lambda data: np.fft.fft2(data)

img = Image.open('images/mit_noise_periodic.jpg')
img = np.array(img)

shape = img.shape[0]*2, img.shape[1]*2
I_bg = np.zeros(shape);
I_bg[0:img.shape[0],0:img.shape[1]] = img

img = np.array(I_bg)
# G = fp.fft2(I_bg);

G = im2freq(I_bg);
G = np.fft.fftshift(G);
G = 20*np.log(np.abs(G))
h = Image.fromarray(G).show()
# [u,v] = freqspace(size(G),'meshgrid');
# u = u*size(G,2)/2;
# v = v*size(G,1)/2;
# D = sqrt(u.^2 + v.^2);
# D0 = 30;
# H = zeros(size(G));
# H(D <= D0) = 1; %filtro ideal com corte em 30.
# F = G.*H;
# F = fftshift(F);
# F = real(ifft2(F));
# F = F(1:size(I,1),1:size(I,2));
# imshow(uint8(F))
# H = 1./(1+(D./D0).^(2*n));
#
#
# Image.fromarray(img).show()
