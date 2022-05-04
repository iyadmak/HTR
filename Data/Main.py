from CleanData import CleanData
from SplitData import SplitData
from InputData import ImagePathsLabels
from PrintFunctions import *


##### CleanData
words_list = CleanData()
CleanDataFunc()


##### SplitData
train_samples ,validation_samples ,test_samples = SplitData(words_list)
SplitDataFunc()


##### ImagePathsLabels
train_img_paths, train_labels = ImagePathsLabels(train_samples)
validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)
test_img_paths, test_labels = ImagePathsLabels(test_samples)
ImagePathsLabelsFunc()
