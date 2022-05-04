from CleanData import CleanData
from SplitData import SplitData
from InputData import ImagePathsLabels

##### FunctionsCalled()

words_list,words = CleanData()

train_samples ,validation_samples ,test_samples = SplitData(words_list)

train_img_paths, train_labels = ImagePathsLabels(train_samples)
validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)
test_img_paths, test_labels = ImagePathsLabels(test_samples)


##### PrintFunctions()

def MainFunc():
    print("\n ###### Preprocess Data ###### \n")

def CleanDataFunc():
    print("     ✅  Clean all errored entries ... ")
    print(f"         {len(words_list)} lines selected from {len(words)} \n")


def SplitDataFunc():
    print("     ✅  Split the dataset into three subsets with a 90:5:5 ...")
    print(f"         {len(train_samples)} Training lines")
    print(f"         {len(test_samples)} Test lines ")
    print(f"         {len(validation_samples)} Validation lines \n")

def ImagePathsLabelsFunc():
    print("     ✅  Generate lists of paths & image names ...\n")