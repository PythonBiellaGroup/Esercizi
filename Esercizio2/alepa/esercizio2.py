# -*- coding: utf-8 -*-
"""

funzione contatore_parole_file() che prende un file name in input 
e ritorna un dizionario contenente i contatori per ciascuna parola. 
PS: rimuovere tutte le punteggiature, tutto in minuscolo
contatore_parole_file('sonetto.txt') => 
{ 'la': 4, 
  'nebbia': 2, ... }

"""
import argparse
import chardet

def replace_special_chars(st ):
    characters = '!?-.:;-,><=»'
    replace_char=" "
    for c in characters:
        st = st.replace(c, replace_char)
    return st   

def remove_duplicate(duplicate): 
    final_list = [] 
    for w in duplicate: 
        if w not in final_list: 
            final_list.append(w) 
    return final_list

def countword(filename):


    try:
       with open(filename, "rb") as f:
          contents = f.read()
    except IOError:
       print ("Error: Could not read file:", filename)

          
    enc = chardet.detect(contents)['encoding'] 
    
    
    with open(filename, "r",encoding=enc) as f:
        contents = f.read().strip().lower()
        contents = replace_special_chars(contents)
        # list
        wordlist = contents.split()
                     
    dict_words = {}
    
    for words in wordlist : 
        dict_words[words] = wordlist.count(words)
    #print('Dictionary\n',dict_words)
    
    dict_words_sorted = {k: v for k, v in sorted(dict_words.items(), key = lambda item: item[1], reverse=True)}
    print('SORTED\n',dict_words_sorted)
       

## main        

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-t", "--text", required=True, help="path to text file")

args = vars(ap.parse_args())  

name = args["text"]

countword(name)

