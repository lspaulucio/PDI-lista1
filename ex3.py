# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 09/05/19
"""

from PIL import Image
import numpy as np
import MyLib as ml


img = Image.open('images/Fig4.19(a).jpg')
img = np.array(img)

imgMed = ml.conv2D(img, ml.MEAN_FILTER2)            # Filtro media ponderada
# histograma = ml.calculaHistograma(img)            # Comentado, pois foi utilizado para escolher o threshold
# plt.plot(histograma[0], histogram[1])
# plt.show()
imgBin = ml.binarizaImg(imgMed, 200)                # Binarizacao da imagem
im = ml.conv2D(imgBin, ml.LAPLACE_FILTER)           # Filtro Laplaciano

images = [img, imgMed, imgBin, im]
titles = ["Imagem Original", "Resultado após Filtro Média Ponderada", "Imagem Binarizada", "Filtro Laplaciano"]
ml.show_images(images, 2, titles)
