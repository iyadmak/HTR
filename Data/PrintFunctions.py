from CleanData import CleanData
from SplitData import SplitData
from InputData import ImagePathsLabels
from PrepareLabels import PrepareLabels

##### FunctionsCalled()




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
    global train_labels,validation_labels,test_labels
    train_img_paths, train_labels = ImagePathsLabels(train_samples)
    validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)
    test_img_paths, test_labels = ImagePathsLabels(test_samples)

    print(f'''✅  lists Generated Successfully ''')



def PrepareLabelsFunc():

    print(" \n💡 Prepare Labels ... \n")

    train_CleanedLabels,train_characters,train_max_len = PrepareLabels(train_labels)
    test_CleanedLabels,test_characters,test_max_len= PrepareLabels(test_labels)
    validation_CleanedLabels,validation_characters,validation_max_len = PrepareLabels(validation_labels)
    
    print(f'''\n✅  training data -> Maximum length: {train_max_len}
                    Vocab size : {len(train_characters)}''')

    print(f'''✅  Testing data -> Maximum length: {test_max_len}
                  Vocab size : {len(test_characters)}''')

    print(f'''✅  Validation data -> Maximum length: {validation_max_len}
                  Vocab size : {len(validation_characters)}''')