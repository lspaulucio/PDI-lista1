import numpy as np
from PIL import Image
from MyLib import paddingImage
import matplotlib.pyplot as plt

img = Image.open("images/ruidosa2.tif")
img = np.array(img)

plt.imshow(paddingImage(img, 10, 'repeat'), cmap='gray', interpolation='gaussian')
plt.show()
