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
ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cvshow('dst',th1)
dst=cv2.cornerHarris(th1,2,3,0.04)
print('dst.shape',dst.shape)

#做一个非极大值抑制，
#对比几种情况，当dst越大的时候，角点更容易出现，否则边界会出现很多
orig1=img.copy()
orig2=img.copy()
orig3=img.copy()
orig1[dst>0.02*dst.max()]=[0,0,255]
orig2[dst>0.02*dst.max()]=[0,0,255]
orig3[dst>0.02*dst.max()]=[0,0,255]

res=np.hstack((orig1,orig2,orig3))
cvshow('dst',res)

