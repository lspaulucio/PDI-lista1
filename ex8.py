# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 09/05/19
"""

from PIL import Image
import numpy as np
import MyLib as ml

img1 = Image.open('images/ruidosa1.tif')
img1 = np.array(img1)

img2 = Image.open('images/ruidosa2.tif')
img2 = np.array(img2)

imgOrig = Image.open('images/original.tif')
imgOrig = np.array(imgOrig)

padding_size = ml.getPaddingSize(img1.shape, (11, 11))
img1Media = ml.conv2D(img1, ml.MEAN_FILTER_11, padding=padding_size, padding_type='repeat')
img1Mediana = ml.medianFilter(img1, (11, 11), padding_size, padding_type='repeat')
img1MedianaAdaptativa = ml.adaptativeMedian(img1, (17, 17))

titles1 = ["Imagem Original: ruidosa1.tif", "Filtro Média (11x11)", "Filtro Mediana (11x11)", "Filtro Mediana Adaptativa"]
images1 = [img1, img1Media, img1Mediana, img1MedianaAdaptativa]

print("PSNR da imagem: ruidosa1.tif")
print("Original: {}".format(ml.PSNR(imgOrig, img1)))
print("Media: {}".format(ml.PSNR(imgOrig, img1Media)))
print("Mediana: {}".format(ml.PSNR(imgOrig, img1Mediana)))
print("Mediana Adaptativa: {}".format(ml.PSNR(imgOrig, img1MedianaAdaptativa)))

padding_size = ml.getPaddingSize(img2.shape, (11, 11))
img2Media = ml.conv2D(img2, ml.MEAN_FILTER_11, padding=padding_size, padding_type='repeat')
img2Mediana = ml.medianFilter(img2, (11, 11), padding_size, padding_type='repeat')
img2MedianaAdaptativa = ml.adaptativeMedian(img2, (17, 17))

titles2 = ["Imagem Original: ruidosa2.tif", "Filtro Média (11x11)", "Filtro Mediana (11x11)", "Filtro Mediana Adaptativa"]
images2 = [img2, img2Media, img2Mediana, img2MedianaAdaptativa]

print("PSNR da imagem: ruidosa2.tif")
print("Original: {}".format(ml.PSNR(imgOrig, img2)))
print("Media: {}".format(ml.PSNR(imgOrig, img2Media)))
print("Mediana: {}".format(ml.PSNR(imgOrig, img2Mediana)))
print("Mediana Adaptativa: {}".format(ml.PSNR(imgOrig, img2MedianaAdaptativa)))

ml.show_images(images1, 2, titles1)
ml.show_images(images2, 2, titles2)
