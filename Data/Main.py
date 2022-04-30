from CleanData import CleanData
from SplitData import SplitData
from DataInput import ImagePathsLabels


words_list = CleanData()


train_samples ,validation_samples ,test_samples = SplitData(words_list)

train_img_paths, train_labels = ImagePathsLabels(train_samples)
validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)
test_img_paths, test_labels = ImagePathsLabels(test_samples)


for i in range(5):
    print(train_img_paths[i])
    print(train_labels[i])