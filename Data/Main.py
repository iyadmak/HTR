from CleanData import CleanData
from SplitData import SplitData
from InputData import ImagePathsLabels


words_list = CleanData()
print("\n ✅  Clean all errored entries ... ")

train_samples ,validation_samples ,test_samples = SplitData(words_list)

print(" ✅  Split the dataset into three subsets with a 90:5:5 ...")

train_img_paths, train_labels = ImagePathsLabels(train_samples)
validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)
test_img_paths, test_labels = ImagePathsLabels(test_samples)

print(" ✅  Generate lists of paths & image names ...\n")