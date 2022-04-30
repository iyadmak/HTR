#split the dataset into three subsets with a 90:5:5

def SplitData(words_list) : 

    FirstSplit = int(0.9 * len(words_list))
    train_samples = words_list[:FirstSplit]
    test_samples = words_list[FirstSplit:]

    SecondeSplit = int(0.5 * len(test_samples))
    validation_samples = test_samples[:SecondeSplit]
    test_samples = test_samples[SecondeSplit:]

    return train_samples ,validation_samples ,test_samples