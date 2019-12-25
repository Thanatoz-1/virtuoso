# Virtuoso
> Named Entity BOI tagger for everyone

In this project we are going to create a Named Entity Tagger and Generator tool for creating your own synthetic dataset. Feel free to talk about different styles of creating the dataset if find my idea invalid. This will be a python script that could be used to enter the templates in text format and then generate CSV files from the same templates. 

Targetted input formats
```bash
python virtuso.py templates/template1.txt generated/generated1.txt 
```

This is going to take a text file as an input having data arranged in the following format
```text
{number_of_template_repeatations} Sentence with [variable_label:file_name]
```
The variable_label_name will be the name you want to provide to the token. The script will handle the text accordingly and generate the output in the provided path name. In order to see an example yourself, switch to the [sample1](https://github.com/Thanatoz-1/virtuoso/tree/sample1) branch.