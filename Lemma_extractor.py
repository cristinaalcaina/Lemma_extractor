
import os.path


def extract_list(data):
    output_list = []

    for x in data:
        row = x[:-1].split("\t")
        new_word = {
            "word": row[0], 
            "class": row[1], 
            "frequency": int(row[2])
        }

        output_list.append(new_word)

    return output_list 




"""
Reading input files.

Requirements:
- Files must exist
- Files must have the following structure:

    word1    word_class1    corpus_frequency1
    word2    word_class2    corpus_frequency2
    word3    word_class3    corpus_frequency3
"""
# First file
first_list = input("Enter file path to first list: ")

if os.path.isfile(first_list):
    list_a = open(first_list, "r")
    word_list_a = list_a.readlines() 
else:
    print(f"{first_list} could not be found")
    exit(0)

# Second file
second_list = input("Enter file path to second list: ")
if os.path.isfile(second_list):
    list_b = open(second_list, "r")
    word_list_b = list_b.readlines() 
else:
    print(f"{second_list} could not be found")
    exit(0)


output = open("result.txt","a+")
output.truncate(0)


# Cleaning lists
dict_a = extract_list(word_list_a)
dict_b = extract_list(word_list_b)
output_list = []
for word_a in dict_a:
    for word_b in dict_b:
        if word_a.get('word') == word_b.get('word'):
            output.write(f"{word_a.get('word')}\t{word_a.get('class')}\t{word_a.get('frequency')}\t{word_b.get('class')}\t{word_b.get('frequency')}\n")

list_a.close()
list_b.close()
output.close()


