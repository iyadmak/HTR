from CleanData import CleanData

words_list = CleanData()

FirstSplit = int(0.9 * len(words_list))
train_samples = words_list[:FirstSplit]
test_samples = words_list[FirstSplit:]

SecondeSplit = int(0.5 * len(test_samples))
validation_samples = test_samples[:SecondeSplit]
test_samples = test_samples[SecondeSplit:]