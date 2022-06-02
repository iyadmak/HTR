from PIL import Image
import pandas as pd
import numpy as np
import os

def ExtractData(*FileNames : str) :

    """
    to use extractData Func u need to passe file name as mentioned below
    test_CleanedLabels = ExtractData('test_CleanedLabels')
    """

    AllData =[]
    dir = '../Data'
    

    
    try : 
        
        for FileName in FileNames :
            FileName +=".txt"
            data = []
            with open(os.path.join(dir,FileName), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    data.append(line.split("\n")[0])
                f.close()
            AllData.append(data)
    except Exception as e : 
        print(e)
    
    return AllData


#Resize Function
def resizeImages(images, img_size : tuple):
    
    ResizedImages  = []

    for image in images : 
        img = Image.open(image)
        ResizedImage = img.resize(img_size)
        #print(img.size,ResizedImage.size)
        ResizedImages.append(np.array(ResizedImage))
    return np.array(ResizedImages)

def ConvertToCat(data) :
    return np.array(pd.get_dummies(data))


def ReshapeData(*arr):

    AllData = []
    for data in arr : 
        data = data.reshape(data.shape[0],-1)
        data = data.astype('float32')
        data /= 255
        AllData.append(data)

    return AllData
   

    






