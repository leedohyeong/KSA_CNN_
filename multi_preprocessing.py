# practice
import shutil
from random import seed
from random import random
from random import shuffle
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def search(dirname):
    img_list = []
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.jpg':
                img_list.append(path+'/'+filename)
    return img_list

seed(1)
data_set = './natural_images_data/'
subdirs = ['train/', 'val/', 'test/']
labeldirs = ['airplane/', 'car/', 'cat/', 'dog/', 'flower/', 'fruit/', 'motorbike/', 'person/']
train_ratio = 0.8
val_test_ratio = 0.1
img_list_1 = search("./input/natural_images/airplane")
img_list_3 = search("./input/natural_images/cat")
img_list_2 = search("./input/natural_images/car")
img_list_4 = search("./input/natural_images/dog")
img_list_5 = search("./input/natural_images/flower")
img_list_6 = search("./input/natural_images/fruit")
img_list_7 = search("./input/natural_images/motorbike")
img_list_8 = search("./input/natural_images/person")
shuffle(img_list_1)
shuffle(img_list_2)
shuffle(img_list_3)
shuffle(img_list_4)
shuffle(img_list_5)
shuffle(img_list_6)
shuffle(img_list_7)
shuffle(img_list_8)

final_list = []

for i in range(1, 9):
    exe_str = f"final_list.append(img_list_{i})"
    eval(exe_str)


for sub in subdirs:
    for labelsub in labeldirs:
        dir_name = data_set + sub + labelsub
        # print(dir_name)
        createFolder(dir_name)
for path_list in final_list:
    for i in range(len(path_list)):
        dst_name = path_list[i].split('/')[-1]
        dst_final = dst_name.split('_')[0] + '/'
        if i < int(len(path_list) * train_ratio):
            # print("train_ratio:{}".format(int(len(path_list) * train_ratio)))
            dst = data_set + 'train/' + dst_final + path_list[i].split('/')[-1]
            shutil.move(path_list[i], dst)
            val_count = i
            val_max = val_count + int(len(path_list) * val_test_ratio)
            # print("val_ratio:{}".format(val_max))
        elif val_count < val_max:
            dst_val = data_set + 'val/' + dst_final + path_list[i].split('/')[-1]
            shutil.move(path_list[i], dst_val)
            val_count += 1
        else:
            dst_test = data_set + 'test/' + dst_final + path_list[i].split('/')[-1]
            shutil.move(path_list[i], dst_test)

