from tqdm import tqdm  as bar
import numpy as np
import os


def CleanData():
    
    words_list = []

    path = "/Users/book/Downloads/PFE/Outils/IAM_Dataset/ascii"
    words = open(f"{path}/words.txt", "r").readlines()

    

    for line in bar(words):
        if line[0] == "#":
           
            continue

        if line.split(" ")[1] != "err":  
            words_list.append(line)
            
    #print(len(words_list))

    
    np.random.shuffle(words_list)

    return words_list ,words


def SplitData(words_list) : 

    FirstSplit = int(0.9 * len(words_list))
    train_samples = words_list[:FirstSplit]
    test_samples = words_list[FirstSplit:]

    SecondeSplit = int(0.5 * len(test_samples))
    validation_samples = test_samples[:SecondeSplit]
    test_samples = test_samples[SecondeSplit:]

    return train_samples ,validation_samples ,test_samples

    
def ImagePathsLabels(samples):

    paths = []
    corrected_samples = []
    base_path = "/Users/book/Downloads/PFE/Outils/IAM_Dataset/words"

    
    for  file_line in bar(samples):
        line_split = file_line.strip()
        line_split = line_split.split(" ")

        # Each line split will have this format for the corresponding image:
        # part1/part1-part2/part1-part2-part3.png
        image_name = line_split[0]
        partI = image_name.split("-")[0]
        partII = image_name.split("-")[1]
        img_path = os.path.join(
            base_path, partI, partI + "-" + partII, image_name + ".png"
        )
        if os.path.getsize(img_path):
            paths.append(img_path)
            corrected_samples.append(file_line.split("\n")[0])

    return paths, corrected_samples


def PrepareTrainLabels(labels) : 
    CleanedLabels = []
    characters = set()
    max_len = 0

    for label in bar(labels):
        label = label.split(" ")[-1].strip()
        for char in label:
            characters.add(char)

        max_len = max(max_len, len(label))
        CleanedLabels.append(label)
    
    characters = list(characters)
    
    return CleanedLabels,characters,max_len


def CleanLabels(labels):
    cleaned_labels = []
    for label in labels:
        label = label.split(" ")[-1].strip()
        cleaned_labels.append(label)
    return cleaned_labels



