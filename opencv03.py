# -*- coding: utf-8 -*-
"""opencv03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gG15eX3Uw0hyslVql3Y3VfIYH0rweyM_
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread("arvore.jpg", cv2.IMREAD_REDUCED_COLOR_2)
cv2_imshow(image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_image)

blur_image = cv2.GaussianBlur(image, (27, 27), 0)
cv2_imshow(blur_image)

#filtro sépia
filtroSep = np.array([[0.272, 0.534, 0.131],
                   [0.349, 0.686, 0.168],
                   [0.393, 0.769, 0.189]])
sepia_image = cv2.filter2D(image, -1, filtroSep)
cv2_imshow(sepia_image)

inv_gray_image = 255 - gray_image
cv2_imshow(inv_gray_image)

blur_image = cv2.GaussianBlur(inv_gray_image, (21, 21), 0, 0)
cv2_imshow(blur_image)

