





from matplotlib import pyplot as plt
import cv2
import numpy as np
def pltshow(imgs,titles):
    for i in range(len(imgs)):
        plt.subplot(2, len(imgs)/2+1, i + 1), plt.imshow(imgs[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def cvshow(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getimg(path,flag):
    img = cv2.imread(path)
    b, g, r = cv2.split(img)
    img_c = cv2.merge([r, g, b])
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if flag==0:
        return img
# 若要用Matplot显示就先把bgr转换成rgb,img_c显示即可，opencv imshow时仍用img
    elif flag==1:
        return img_c
    elif flag==2:
        return img_g
        
#图像特征harris角点检测
img=getimg('D:/Image_registration/image_date/10724-10724-10724.tiff',0)
print('img.shape',img.shape)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#dst=cv2.cornerHarris(gray,2,3,0.04)



# SIFT检测器
sift = cv2.SIFT_create()

# 找出图像中的关键点
kp = sift.detect(gray, None)

# 在图中画出关键点
img = cv2.drawKeypoints(gray, kp, img)  
cvshow('dst',img)
'''
# 计算关键点对应的SIFT特征向量
kp, des = sift.compute(gray, kp)   

# 上面的两步，也可以用下面的一步
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray, None)   # 这里还能一步到位，直接算出关键点以及关键向量

'''
