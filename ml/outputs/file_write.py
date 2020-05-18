import csv

def write2file(filename,resultList):
    """
    Writes the output class to the txt file.
    Parameters
    ----------
    filename : str
        Output file name.
    resultList :
        Actual output of the test set from the trained classifier.
    Returns
    -------
    None
    """
    with open(filename,'w',newline='') as outputFile:
        writer = csv.writer(outputFile)
        for result in resultList:
            writer.writerow([result])
