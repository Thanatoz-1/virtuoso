from argparse import ArgumentParser

def Parser():
    '''
    This is the function to parse your arguments into a more understable form and 
    provide relavant help whenever needed.

    The package usage are as follows:
    python virtuoso <path_to_templates> <path_to_outputs>

    <path_to_templates> is the path to the text file having templates as mentioned 
    in the README file.
    
    <path_to_generated> is the file path and the file name in which the csv needs to be 
    stored.

    The script is compatible with python>3.5.2 
    '''
    parser = ArgumentParser()
    parser.add_argument("Text_file_path", help = ".txt file relative path // in which templates are stored")
    parser.add_argument("Output_file_path", help = "relative path of file where data is to be stored")
    args = parser.parse_args()

    textPath = args.Text_file_path
    # Append a txt extention to the templates file if not specified
    textPath = textPath+'.txt' if len(textPath.split('.')) == 1 else textPath 

    savePath = args.Output_file_path
    # Append a csv extention to the templates file if not specified
    savePath = args.Output_file_path +'.csv' if len(savePath.split('.')) == 1 else args.Output_file_path

    return textPath, savePath

if __name__=='__main__':
    textPath, savePath = Parser()

    # Reading templates 
    with open(textPath, 'r') as f:
        textData = f.readlines()
    
    
