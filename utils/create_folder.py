import os

def create_folder(filepath):
    '''
    This function:
        - create a folder required for file
    
    Parameters:
    -----------
    filepath: string - directory path
    
    return:
    -------
    None
    '''
    if not os.path.exists(filepath):
        os.makedirs(filepath)
        print(filepath)
    else:
        pass
        
