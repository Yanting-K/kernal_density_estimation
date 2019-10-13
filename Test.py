from load_file import*

train_data,rows,cols,dims = load_img(input_dir)
ff =np.load('train.npy')
g = np.zeros((rows,cols))
for i in range(rows):
    for j in range(cols):
        if ff[i,j]<2*10**(-7):
            g[i,j] = 255
        else:
            g[i,j] = 0

cv2.imwrite('最后效果图.jpg',g)
