from CleanData import CleanData
from SplitData import SplitData
from InputData import ImagePathsLabels
from PrintFunctions import *

##### MainFunc()
MainFunc()

##### CleanData
words_list,words = CleanData()
CleanDataFunc()


##### SplitData
SplitDataFunc()


##### ImagePathsLabels
train_img_paths, train_labels = ImagePathsLabels(train_samples)
validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)
test_img_paths, test_labels = ImagePathsLabels(test_samples)
ImagePathsLabelsFunc()
