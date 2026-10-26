import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("Me.jpeg")

(h, w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated)
plt.title("Rotated Image")
plt.show()

brightness_Matrix = np.ones(image.shape, dtype="uint8") * 80
brighter = cv2.add(image, brightness_Matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter)
plt.title("Brighter image")
plt.show()