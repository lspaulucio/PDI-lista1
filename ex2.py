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
img_result = ml.conv2D(img, ml.LAPLACE_FILTER2)
img_lowfilter = ml.conv2D(img, ml.MEAN_FILTER)

titles = ["Imagem Original", "Filtro passa baixa (média)", "Filtro Laplaciano", "Resultado Final utilizando o filtro de Laplace"]
images = [img, img_lowfilter, img_laplace, img_result]

ml.show_images(images, 2, titles, False)
