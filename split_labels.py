# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 20:22:32 2018

@author: LXY
"""
import numpy as np
import pandas as pd

'''change here'''
path = 'D:\\Database\\Transmission_lines\\Insulator\\Drop_off\\256roi_64test_192train'

full_labels = pd.read_csv(path+'\\CSV_tfrecord\\all_labels.csv')
full_labels.head()

grouped = full_labels.groupby('filename')
grouped.apply(lambda x: len(x)).value_counts()

gb = full_labels.groupby('filename')
grouped_list = [gb.get_group(x) for x in gb.groups]
len(grouped_list)

'''change here'''
#随机取160个作为train，剩下的40个作为测试
train_index = np.random.choice(len(grouped_list), size=192, replace=False)
test_index = np.setdiff1d(list(range(256)), train_index)
len(train_index), len(test_index)

# take first 200 files
train = pd.concat([grouped_list[i] for i in train_index])
test = pd.concat([grouped_list[i] for i in test_index])
len(train), len(test)
#这里输出不知道为什么是173,44,因为一张图可能不止一个目标

#转换成csv
train.to_csv(path+'\\CSV_tfrecord\\train_labels.csv', index=None)
test.to_csv(path+'\\CSV_tfrecord\\test_labels.csv', index=None)
print('Successfully split label for :',len(train_index),'train','and' ,len(test_index),'test')
