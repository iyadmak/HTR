import os

def ExtractData(FileName : str) :

    """
    to use extractData Func u need to passe file name as mentioned below
    test_CleanedLabels = ExtractData('test_CleanedLabels')
    """

    data = []
    dir = '../Data'
    FileName +=".txt"

    
    try : 
       
        with open(os.path.join(dir,FileName), 'r') as f:
            lines = f.readlines()
            for line in lines:
                data.append(line.split("\n")[0])
            f.close()
        
    except Exception as e : 
        print(e)
    
    return data