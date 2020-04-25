#!/usr/bin/env python3

##########################################################################
#Write a counter_words_file () function that takes an input file name and returns a dictionary containing the counters for each word.
#PS: remove all punctuation, all in lowercase

#contatore_parole_file ('sonetto.txt') => {'la': 4, 'fog': 2, ...}

##########################################################################
# get character detection library
# install with:   pip install chardet
import chardet

# used to extract filenames (without using much regex)
import glob

# used to get commandline arguments (only a comment in this program)
import sys

# remove chars causing trouble for split
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~’»«'''
# —

def contatore_parole_file( fname ):
    # create dictionary
    mydict = {}
    maxoccurancesofword = 0

    # open the file, read the data into a string, remove CR and convert to lowercase
    # sonetto.txt:  UTF-8 Unicode text, with CRLF line terminators
    # sonetto3.txt: ISO-8859 text, with CRLF line terminators

    # open the file as a binary file and read all data
    with open(fname, 'rb') as f:
        rawdata = f.read()

    # Guess! the encoding, normally OK. Store value found in enc
    # errorhandling missing if encoding is not found
    enc = chardet.detect(rawdata)['encoding']

    # read all file into content
    with open(fname, 'r', encoding=enc) as f:
        content = f.read().replace('\n', ' ').lower()

    # remove all punctuation
    for char in content:
        if char in punctuations:
            content = content.replace(char," ")

    # split string into a list of words
    listofwords = content.split()

    # count the occurances of the word in the string
    for word in listofwords:
        if word in mydict:
            mydict[word] = mydict[word] + 1
            if mydict[word] > maxoccurancesofword:
                maxoccurancesofword = maxoccurancesofword + 1
        else:
            mydict[word] = 1

    # display dictionary ( not sorted )
    #print(mydict, sep=" : ")

    # display filename and dictionary sorted
    sortdict = {}
    for index in range( 1, maxoccurancesofword+1 ):
        for key in mydict.keys():
            if mydict[key] == index:
                sortdict[key] = mydict[key]

    print(fname, sortdict, sep=" : ")
# ready for next file

# main code
# read all *.txt files in directory
for fname in glob.glob("*.txt"):
    contatore_parole_file( fname )

# alternative to for statement
# open the file specified as parameter 1
#import sys
#contatore_parole_file( sys.argv[1] )

