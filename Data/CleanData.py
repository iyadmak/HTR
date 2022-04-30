#Clear all errored entries
from fastapi import Path
import numpy as np

def CleanData():
    
    words_list = []

    path = "/Users/book/Downloads/PFE/Outils/IAM_Dataset/ascii"
    words = open(f"{path}/words.txt", "r").readlines()

    for line in words:
        if line[0] == "#":
            continue
        if line.split(" ")[1] != "err":  
            words_list.append(line)

    #print(len(words_list))

    
    np.random.shuffle(words_list)

    return words_list

