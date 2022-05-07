import os

def ExtractData(FileName : str) :

    dir = '../Data'
    FileName +=".txt"
    
    try : 
       
        with open(os.path.join(dir,FileName), 'r') as f:
            lines = f.readlines()
            
            f.close()
        
    except Exception as e : 
        print(e)
    
    return lines