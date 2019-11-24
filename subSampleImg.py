import cv2 as cv
import os

def imagePath(dir):
    list=[]
    pathDir=os.listdir(dir)
    for filePath in pathDir:
        filePathGroup=os.path.join(dir,filePath)
        list.append(filePathGroup)
    return list

def subsampled(filePath,verticalAxis,horizontalAxis):
    fileGroup=imagePath(filePath)
    appendFilePath="img"+str(verticalAxis)+"_"+str(horizontalAxis)+"//"
    resImgPath=os.path.join(filePath,appendFilePath)
    if not os.path.exists(resImgPath):
        print("create the directory "+resImgPath)
        os.makedirs(resImgPath)
        pathDir=os.listdir(filePath)
        i=0
        for file in fileGroup:
            try:
                img=cv.imread(file)
                resImg=cv.resize(img,(verticalAxis,horizontalAxis),interpolation=cv.INTER_CUBIC)
                cv.imwrite(resImgPath+pathDir[i],resImg)
                i=i+1
                print(resImgPath)

            except :
                print(file+" is created error")
            print(file+" is created successful")

for i in range(8,15,1):
    subsampled(r"C:\Users\pcb17\Desktop\gratuatePaper\faceLibrary\F6BA0D84_1A89_4E53_B353_13D195F6A00E\dataSet\cmu",i,i)
    subsampled(r"C:\Users\pcb17\Desktop\gratuatePaper\faceLibrary\F6BA0D84_1A89_4E53_B353_13D195F6A00E\dataSet\feret",i,i)
    subsampled(r"C:\Users\pcb17\Desktop\gratuatePaper\faceLibrary\F6BA0D84_1A89_4E53_B353_13D195F6A00E\dataSet\orl",i,i)
    subsampled(r"C:\Users\pcb17\Desktop\gratuatePaper\faceLibrary\F6BA0D84_1A89_4E53_B353_13D195F6A00E\dataSet\yale",i,i)