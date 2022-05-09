import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from PIL import Image

# 1、灰度化
img = cv2.imread('lenna.png')    # 引入图像lenna.png
h, w = img.shape[:2]             # 将高和宽赋值给h,w
img_gray = np.zeros([h, w], img.dtype)   # 复制一个等比例图像图像
for i in range(h):
    for j in range(w):
        m = img[i, j]
        img_gray[i, j] = int(m[0] * 0.11 + m[1] * 0.59 + m[2] * 0.3)  # 图像灰度化
print(img_gray)
print("image show gray: %s" % img_gray)
cv2.imshow("image list x", img_gray)

# 用rgb2gray库直接将图片灰度化
img_gray = rgb2gray(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGRGRAY)
img_gray = img
plt.subpolot(222)
plt.inshow(img_gray, cmap='gray')
print("---image gray----")
print(img_gray)


plt.subplot(221)
img = plt.imread("lenna.png")
img = cv2.imread("lenna.png", False)
plt.imshow(img)
print("---image lenna----")
print(img)


# 二值化
rows, cols = img_gray.shape
for i in range(rows):
    for j in range(cols):
        if img_gray[i, j] <= 128:  # 这里不知道为什么只有0和255才能把图片二值化
            img_gray[i, j] = 0
        else:
            img_gray[i, j] = 255
print(img_gray)
cv2.imshow("image list", img_gray)
cv2.waitKey()


img_binary = np.where(img_gray >= 128, 255, 0)   # 对img_gray进行二值化用numpy的内置函数where
print("-----image_binary------")
print(img_binary)
print(img_binary.shape)
cv2.imshow("image list", img_binary)
cv2.waitKey()


