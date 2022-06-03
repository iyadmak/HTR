from PreprocessFile import *
from tqdm import tqdm as bar
import os


def MainFunc():
    print("\n ############ Preprocess Data ############ \n")


def CleanDataFunc():

    global words_list,words
    print('💡 Clean all errored entries ... \n')
    
    try : 
        words_list,words = CleanData()
    except Exception as e : 
        print(e)
    else : 
        print(f"\n✅ {len(words_list)} lines selected from {len(words)}")


def SplitDataFunc():
    global train_samples ,validation_samples ,test_samples

    print("\n💡 Split the dataset into three subsets with a 90:5:5 ...")
    try : 
        train_samples ,validation_samples ,test_samples = SplitData(words_list)
    except Exception as e : 
        print(e)
    else : 
        print(f'''     
✅ {len(train_samples)} Training lines
✅ {len(test_samples)} Test lines
✅ {len(validation_samples)} Validation lines ''')


def ImagePathsLabelsFunc():

    print("\n💡 Generate lists of paths & image names ...\n")
    global train_img_paths,train_labels,test_img_paths,test_labels,validation_img_paths,validation_labels
    
    try : 
        train_img_paths, train_labels = ImagePathsLabels(train_samples)
        test_img_paths, test_labels = ImagePathsLabels(test_samples)
        validation_img_paths, validation_labels = ImagePathsLabels(validation_samples)
    except Exception as e : 
        print(e)
    else : 
        print(f'''\n✅  lists Generated Successfully ''')


def PrepareLabelsFunc():

    print(" \n💡 Prepare Labels ... \n")
    
    global train_CleanedLabels,characters,max_len,max_label,test_CleanedLabels,test_CleanedLabels,validation_CleanedLabels
    
    try :     

        train_CleanedLabels = CleanLabels(train_labels)
        test_CleanedLabels = CleanLabels(test_labels)
        validation_CleanedLabels = CleanLabels(validation_labels)
        
        characters,max_len,max_label = Nb_Len_Labels(train_CleanedLabels,test_CleanedLabels,validation_CleanedLabels)
        
        
   
    except Exception as e : 
        print(e)
    else : 
        print(f'''

✅  {len(train_CleanedLabels)} Cleaned labels 
✅  {len(characters)} Character
✅  {max_len} Maximum word length  ''')
    

def DataFilesGenerator ():
    
    print(" \n💡 Generate the Files of Data ... \n")

    data = [train_img_paths,train_CleanedLabels,characters,max_len,max_label,test_img_paths,test_CleanedLabels,validation_img_paths,validation_CleanedLabels]    
    names = ["train_img_paths","train_CleanedLabels","characters","max_len","max_label","test_img_paths","test_CleanedLabels","validation_img_paths","validation_CleanedLabels"]    
    
    ## Create new dir

    if os.path.basename(os.getcwd()) == "preprocess" or os.path.basename(os.getcwd()) == "src": 
        os.chdir("..")
    
    directory = "Data"
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    

    try : 
    
        for i in bar(range(len(data))) :
            lines = data[i]  
            
            if data[i] != max_len and  data[i] != max_label :
                with open(os.path.join(path,f"{names[i]}.txt"), 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
            else :
                with open(os.path.join(path,f"{names[i]}.txt"), 'w') as f:
                        f.write(str(data[i]))
            
            f.close()
            

    except Exception as e : 
        print(e)
    else : 
        print("\n✅  Data Files generated Successfully \n") 

    