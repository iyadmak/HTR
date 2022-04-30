#Clear all errored entries
import numpy as np

def CleanData():
    
    words_list = []

    base_path = "/Users/book/Downloads/PFE/Outils/IAM_Dataset/ascii"
    words = open(f"{base_path}/words.txt", "r").readlines()

    for line in words:
        if line[0] == "#":
            continue
        if line.split(" ")[1] != "err":  
            words_list.append(line)

    #print(len(words_list))

    
    np.random.shuffle(words_list)

    return words_list

