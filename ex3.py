# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import MyLib as ml
import matplotlib.pyplot as plt

img = Image.open('images/Fig4.19(a).jpg')
img = np.array(img)
img = ml.conv2D(img, ml.MEAN_FILTER2)
Image.fromarray(img).show()

histograma = ml.calculaHistograma(img)
plt.plot(histograma)
plt.show()

im = ml.binarizaImg(img, 200)
Image.fromarray(im).show()

im = ml.conv2D(im, ml.LAPLACE_FILTER)
Image.fromarray(im).show()
