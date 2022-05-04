from tqdm import tqdm  as bar

def PrepareLabels(labels) : 
    CleanedLabels = []
    characters = set()
    max_len = 0

    for label in bar(labels):
        label = label.split(" ")[-1].strip()
        for char in label:
            characters.add(char)

        max_len = max(max_len, len(label))
        CleanedLabels.append(label)

    return CleanedLabels,characters,max_len
    '''print("Maximum length: ", max_len)
    print("Vocab size: ", len(characters))'''

