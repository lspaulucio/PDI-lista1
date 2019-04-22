from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def conta(img, i, j):
    print(i,j)


def contaPalito(img):
    shape = img.shape

    col = shape[0]/2

    for i in range(0, shape[2]):
        if(img[i][col] == 255):
            conta(img, i, col)


img = Image.open('images/Fig8.02.jpg')
# plt.figure()
# plt.plot(img.histogram())

img = np.array(img)
# print(img)
histograma = np.zeros(256)

shape = img.shape
for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        histograma[img[i][j]] += 1

# plt.figure(2)
# plt.plot(histograma)
# plt.show()

THRESHOLD = 160

for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        if (img[i][j] >= THRESHOLD):
            img[i][j] = 255
        else:
            img[i][j] = 0

im = Image.fromarray(img)
im.show()
