from PreprocessFile import *


##### PrintFunctions()

def MainFunc():
    print("\n ############ Preprocess Data ############ \n")


def CleanDataFunc():

    global words_list,words
    print('💡 Clean all errored entries ... \n')
    words_list,words = CleanData()
    print(f"\n✅ {len(words_list)} lines selected from {len(words)}")


def SplitDataFunc():
    global train_samples ,validation_samples ,test_samples

    print("\n💡 Split the dataset into three subsets with a 90:5:5 ...")

    train_samples ,validation_samples ,test_samples = SplitData(words_list)

    print(f'''     
✅ {len(train_samples)} Training lines
✅ {len(test_samples)} Test lines
✅ {len(validation_samples)} Validation lines ''')


def ImagePathsLabelsFunc():

    print("\n💡 Generate lists of paths & image names ...\n")
    global train_img_paths,train_labels,test_img_paths,test_labels,validation_img_paths,validation_labels
    
    train_img_paths, train_labels = ImagePathsLabels(train_samples)
    test_img_paths, test_labels = ImagePathsLabels(test_samples)
    validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)

    print(f'''\n✅  lists Generated Successfully ''')


def PrepareLabelsFunc():

    print(" \n💡 Prepare Labels ... \n")
    global train_CleanedLabels,train_characters,train_max_len,test_CleanedLabels,test_CleanedLabels,validation_CleanedLabels
    
    train_CleanedLabels,train_characters,train_max_len = PrepareTrainLabels(train_labels)
    test_CleanedLabels = CleanLabels(test_labels)
    validation_CleanedLabels = CleanLabels(validation_labels)

    print(f'''
\nTraining data :  

✅  {len(train_CleanedLabels)} Cleaned labels 
✅  {len(train_characters)} Character
✅  {train_max_len} Maximum word length  ''')
    
def ReturnData ():
    """
    the Function will return respectively train_img_paths,train_CleanedLabels,
                                          train_characters,train_max_len,
                                          test_img_paths,test_CleanedLabels,
                                          validation_img_paths,validation_CleanedLabels 
    """
    return train_img_paths,train_CleanedLabels,train_characters,train_max_len,test_img_paths,test_CleanedLabels,validation_img_paths,validation_CleanedLabels

    