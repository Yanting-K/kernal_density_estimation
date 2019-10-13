import os
import numpy as np 
import cv2
from load_file import*
from math import *
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def train():
    input_dir = '/home/kyt/桌面/训练数据集/'
    test_dir = '/home/kyt/桌面/测试数据集/frame_0777.jpg'



    train_data,rows,cols,dims = load_img(input_dir)
    test_date = cv2.imread(test_dir)
    test_date = np.asarray(test_date)

    
    f=np.zeros((rows,cols))
    f1=np.empty((rows,cols,dims))
    f2 = np.zeros((rows,cols))    
    high,temp = 100,1
    

    for i in range(20):
        for j in range(rows):
            for k in range(cols):
                for l in range(dims):
                
                    f1[j,k,l]=1-(((test_date[j,k,l]-train_data[j,k,l,i])/float(high))**2)
                    if f1[j,k,l]<0:
                        f1[j,k,l]=0
                    temp = temp*f1[j,k,l]
                f2[j,k] = temp
                temp = 1
        f = f+f2
        print('success '+ str(i))
    f=15/(8*pi*20*high**3)*f

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.linspace(1,rows,rows)
    Y = np.linspace(1,cols,cols)
    X,Y = np.meshgrid(Y,X)
    ax.plot_surface(X,Y,f)
    plt.savefig('KDEresult.png')
    plt.show()
    np.save('train',f)

if __name__=="__main__":

    train()
    
