# -*- coding: utf-8 -*-

""" Processamento Digital de Imagens
    Aluno: Leonardo Santos Paulucio
    Lista de Exercicios 1 - Pós-Graduação
    Data: 09/05/19
"""

from PIL import Image
import numpy as np
from numpy import fft

import MyLib as ml

img = Image.open('images/mar-il.gif')
img = np.array(img)

I_bg = ml.extendImg(img)                           # Criando a imagem estendida de tamanho (2M, 2N)

G = ml.fshift(I_bg)                                # Multiplicando por (-1)^(x+y)
G = fft.fft2(G)                                    # Calcula a DFT

D0 = 80                                            # Frequencia de corte
H = ml.filterHomomorphic(G, D0, yh=2, yl=0.25)     # Criando filtro homomorfico
F = G * H                                          # Convolucao no dominio da frequencia
F = np.real(fft.ifft2(F))                          # Pegando a parte real da dft inversa
F = ml.fshift(F)                                   # Multiplicando por (-1)^(x+y)
F = F[0:img.shape[0], 0:img.shape[1]]              # Pegando a parte superior esquerda

FE = ml.equalizaHistograma(F)                      # Realizando equalizacao do histograma da imagem com filtro homomorfico
G = ml.equalizaHistograma(img)                     # Realizando equalizacao do histograma na imagem original
images = [img, F, G, FE]                           # Lista de imagens a serem imprimidas

# Titulos das imagens
titles = ["Imagem Original", "Resultado com Filtro Homomórfico", "Resultado com Equalização de Histograma",
          "Combinação de Filtro Homomórfico e Equalização de Histograma"]
ml.show_images(images, 2, titles)
