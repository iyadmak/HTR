from CleanData import CleanData
from SplitData import SplitData
from InputData import ImagePathsLabels

words_list,words = CleanData()
train_samples ,validation_samples ,test_samples = SplitData(words_list)

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