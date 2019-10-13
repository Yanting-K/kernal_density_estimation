import sys
import os
import cv2
import numpy as np
from PIL import Image
Img=[]

input_dir = '/home/kyt/桌面/训练数据集/'
def load_img(img_name):
    img = os.listdir(img_name)
    #print(img)
    img.sort(key= lambda x:int(x[7:10]))
    #print(img)
    imgNum = len(img)
    data = np.empty((576,768,3,imgNum))
    for i in range(1):
        imgs = cv2.imread(img_name+'/'+img[i])
        imgdate = np.array(imgs)
  
        r,c,d = imgdate.shape
 
        array = np.asarray(imgs) 
        data[:,:,:,i] = array

    print("success reading !")
    return data,r,c,d
if __name__ =='__main__':
    load_img(input_dir)
