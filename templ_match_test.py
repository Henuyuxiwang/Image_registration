# This script is used to register two images using template matching method.
# Author: yuxi
# Date: 2023-03-29
# 此函数用于测试模板匹配
# 它读取两个图像，从第一个图像中裁剪出一个模板，然后将模板与第二个图像匹配
# 然后显示匹配的图像和裁剪的模板
import cv2
import numpy as np

    # 读参考图像
img0 = cv2.imread("D:/Image_registration/image_date/10450-10450-10450.tiff")
    # img1=imread("D:/Image_registration/image_date/10724-10724-10724.tiff");
img1 = cv2.imread("D:/Image_registration/image_date/10750-10750-10750.tiff")
    # imwrite("D:/Image_registration/image_date/0.tiff", img0);
    # se = translate(strel(1), [50 140]);%将一个平面结构化元素分别向下和向右移动30个位置
    # img1 = imdilate(img1,se);%利用膨胀函数平移图像
# Manually select a region from the first image as a template
rect = cv2.selectROI('roi',img0, False, False)
cv2.destroyAllWindows()
template= img0[int(rect[1]):int(rect[1]+rect[3]), int(rect[0]):int(rect[0]+rect[2])]
cv2.imshow('Selected Region', template)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


result = cv2.matchTemplate(img1, template, cv2.TM_CCOEFF_NORMED)
    # 根据图像的大小，计算空间域或频域中的互相关性。
    # 通过预先计算运行总和来计算局部总和。
    # 使用局部总和来归一化互相关性以获得相关系数。

    # 获取匹配结果
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + int(rect[2]), top_left[1] + int(rect[3]))
    # 获取配准后的图像
img_registered = cv2.rectangle(img1, top_left, bottom_right, (0, 0, 255), 2)

    # 显示配准后的图像
cv2.imshow("img_registered", img_registered)
img_registered1 = img1[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    # 裁剪配准后的图像
cv2.imshow("img_registered1", img_registered1)
cv2.waitKey(0)
cv2.destroyAllWindows()


