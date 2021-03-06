# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 19:40:36 2018

@author: LXY
"""
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    '''change here'''
    path='D:\\Database\\Transmission_lines\\Insulator\\Drop_off\\256roi_64test_192train'
    
    data_path = os.path.join(path, 'Annotations')   #标签的目录
    xml_df = xml_to_csv(data_path)  
    xml_df.to_csv(path+'\\CSV_tfrecord\\all_labels.csv', index=None)     #存放CSV文件目录
    print('Successfully converted xml to csv.')

main()

