# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 19/05/19
"""

from PIL import Image
import numpy as np
import MyLib as ml
import copy

img = Image.open('images/ruidosa2.tif')
img = np.array(img)
imgOld = copy.deepcopy(img)
img_laplace = ml.conv2D(img, ml.MEAN_FILTER3, padding=5) # padding 5 para manter o msm tamanho da imagem original
# img_lowfilter = ml.conv2D(img, ml.MEAN_FILTER)
print(ml.PSNR(imgOld, img_laplace))
Image.fromarray(img_laplace).show(title="Laplaciano")

# Image.fromarray(img_lowfilter).show(title="Filtro passa baixo (média)")
