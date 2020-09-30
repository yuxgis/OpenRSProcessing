'''
Descripttion: 变化监测图像同时裁剪
version: 
Author: CHEN_JIAHAO
Date: 2020-09-29 20:55:36
LastEditors: CHEN_JIAHAO
LastEditTime: 2020-09-30 15:43:41
'''
import numpy as np
import cv2
import os
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib
import scipy 
import scipy.misc
import glob
save_path = r"E:\test\crop_test\OUT"
root = r"E:\test"
before_list = glob.glob(root+"/A" + r"/*.png")
after_list = glob.glob(root+"/B" + r"/*.png")
mask_list = glob.glob(root+"/OUT" + r"/*.png")
for i in range(len(before_list)):
    before_file_name = os.path.split(before_list[i])[-1].split(".")[0]
    after_file_name = os.path.split(after_list[i])[-1].split(".")[0]
    mask_file_name = os.path.split(mask_list[i])[-1].split(".")[0]



    # before_img = cv2.imread(r'E:\test\A\train_1.png')
    before_img = cv2.imread(before_list[i])
    before_img = cv2.cvtColor(before_img, cv2.COLOR_BGR2RGB)
    # after_img = cv2.imread(r'E:\test\B\train_1.png')
    after_img = cv2.imread(after_list[i])
    before_img = cv2.cvtColor(before_img, cv2.COLOR_BGR2RGB)

    # mask = cv2.imread(r'E:\test\OUT\train_1.png')
    mask = cv2.imread(mask_list[i])
    image = np.concatenate([before_img,after_img,mask],axis=2)
    


    print(image.shape)
    print(mask.shape)

    #裁剪
    hight = image.shape[0]
    width = image.shape[1]
    w = 256
    id = 1
    i = 0
    while (i + w <= hight):
        j = 0
        while (j + w <= width):
            #new_img = image.crop((i, j, i + w, j + w))
            new_img = image[i:i + w, j:j + w,:]
            before_img_crop = new_img[:,:,0:3]
            after_img_crop = new_img[:,:,3:6]
            change_img_crop = new_img[:,:,6:9]
            
            save_path = r"E:\test\crop_test\OUT"

            cv2.imwrite(os.path.join(save_path,"A","%s_%s.png"%(before_file_name,str(id))),before_img_crop)
            print(cv2.imwrite(os.path.join(save_path,"A","%s_%s.png"%(before_file_name,str(id))),before_img_crop))
            cv2.imwrite(os.path.join(save_path,"B","%s_%s.png"%(after_file_name,str(id))),after_img_crop)
            print(cv2.imwrite(os.path.join(save_path,"B","%s_%s.png"%(after_file_name,str(id))),after_img_crop))
            cv2.imwrite(os.path.join(save_path,"OUT","%s_%s.png"%(mask_file_name,str(id))),change_img_crop)
            print(cv2.imwrite(os.path.join(save_path,"OUT","%s_%s.png"%(mask_file_name,str(id))),change_img_crop))
            id += 1
            j += w
        i = i + w