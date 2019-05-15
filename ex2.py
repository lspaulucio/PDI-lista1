# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
import MyLib as ml

img = Image.open('images/lena.tif')
img = np.array(img)
img_laplace = ml.conv2D(img, ml.LAPLACE_FILTER)
img_lowfilter = ml.conv2D(img, ml.MEAN_FILTER)

Image.fromarray(img_laplace).show(title="Laplaciano")
Image.fromarray(img_lowfilter).show(title="Filtro passa baixo (média)")
