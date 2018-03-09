import cv2
import os

'''
rename and resize all the images in the filepath 
and save in filepath\JPEGImages\
'''

if __name__=='__main__':
#    path = os.getcwd()
#    imgs = os.listdir(path+"\\kings_test_img\\")
    '''change here'''
    path='Path to img'
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    #目录下如果没有相应的文件夹则新建
    if os.path.exists(path+'//JPEGImages') == False:
        os.mkdir(path+'//JPEGImages')
#    if os.path.exists(path+'//Annotations') == False:
#        os.mkdir(path+'//Annotations')
#    if os.path.exists('ImageSets') == False:
#        os.mkdir('ImageSets')
#        os.mkdir('ImageSets/Main')
    '''may change here'''
    cnt = 1
    prename = "000000"
    for img in filelist:
        imgdir=os.path.join(path,img)
        if os.path.isdir(imgdir):continue   #如果是文件夹则跳过
        print(imgdir)
        temp=cv2.imread(imgdir)             #原来的文件路径     
                 
        #os.remove(path+"\\kings_test_img\\"+img)
        rows,cols,channels = temp.shape
        
        #resize
        temp=cv2.resize(temp,(512,512),cv2.INTER_AREA)
        
        #style:000001.jpg
        cv2.imwrite(path+"\\JPEGImages\\"+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg",temp) 
        
        #style:image1.jpg
        #cv2.imwrite(path+"\\kings_test_img\\"+"image"+str(cnt)+".jpg",temp)   
        print ("renamed "+img+" to "+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg")
        #print ("renamed "+img+" to "+"image"+str(cnt)+".jpg")
        cnt+=1
    print ('done!')