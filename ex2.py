# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 09/05/19
"""

from PIL import Image
import numpy as np
import MyLib as ml


img = Image.open('images/lena.tif')
img = np.array(img)

img_laplace = ml.conv2D(img, ml.LAPLACE_FILTER)  # Realiza a convolução com filtro laplaciano
img_result = ml.conv2D(img, ml.LAPLACE_FILTER2)  # Realiza a convolução com filtro laplaciano ja somando com a imagem
img_lowfilter = ml.conv2D(img, ml.MEAN_FILTER)   # Realiza a convolução com filtro media

titles = ["Imagem Original", "Filtro Passa Baixa (Média)", "Filtro Laplaciano",
          "Resultado Final Utilizando o Filtro de Laplaciano"]
images = [img, img_lowfilter, img_laplace, img_result]
ml.show_images(images, 2, titles, False)
