from argparse import ArgumentParser
import os
import re
from collections import defaultdict
import random
import spacy

nlp = spacy.load('en_core_web_sm')

class DataFetcher:
    def __init__(self):
        BASE='Data/'
        self.tables=os.listdir(BASE)
        self._data = defaultdict(lambda:[])
        for file in self.tables:
            file_name, ext = os.path.splitext(file)
            if ext=='.txt':
                with open(os.path.join(BASE,file),'r') as f:
                    self._data[file_name] = f.readlines()
        
    def getItem(self, filename):
        ret=random.choice(self._data[filename])
        return ret

target = DataFetcher()

def Extractor(keyword, null_token='O'):
    if '[' not in str(keyword):
        return [(tok.text, null_token) for tok in nlp(keyword)]
    e = re.sub('[^0-9a-zA-Z]+',' ', str(keyword)).strip().split()
    value=target.getItem(e[1]).split()
    ret_tok=e[0]
    # [x for b in a for x in b]
    ret=[(int_tok.text, ind, idx, 'I-'+ret_tok) if (ind+idx>0) else (int_tok.text, ind, idx, 'B-'+ret_tok) for ind, ent_tok in enumerate(value) for idx, int_tok in enumerate(nlp(ent_tok))]
    return ret

def process_string(query):
    query=query.replace('\n','').split()
    sentence=[]
    labels=[]
    for token in query:
        extracted=Extractor(token)
        for ent in extracted:
            sentence.append(ent[0])
            labels.append(ent[1])
    res=[]
    for i,j in zip(sentence, labels):
        res.append(str(i)+'###'+str(j))
    return ' '.join(res)
    

def ArgParser():
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
    textPath, savePath = ArgParser()

    # Reading templates 
    with open(textPath, 'r') as f:
        textData = f.readlines()
    mode='a' if os.path.exists(savePath) else 'w'
    header='data'
    count=0
    with open(savePath, mode) as out:
        for line in textData:
            tokens = line.split()
            repeats = 1 if tokens[0].replace("{", "").replace("}", "")=='' else tokens[0].replace("{", "").replace("}", "")
            query=' '.join(tokens[1:])
            res=[]
            for _ in range(int(repeats)):
                res.append(process_string(query))
            print(res)