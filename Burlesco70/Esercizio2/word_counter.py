import re
import argparse
import sys

if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
    # WARNING: Python 3.6 or higher is required to have ordered dictionaries
    from operator import itemgetter
    from collections import OrderedDict

class WordFileCounter():
    """
    Class that returns an ordered (or not) dictionary containing the counts for each word from text file
    """
    def __init__(self, file_name, ordered = False):
        self.file_name = file_name
        self.ordered = ordered

    def __clean(self, sentence):
        # Remove punctuations
        return re.sub(r'[^A-Za-z0-9 ]+', ' ', sentence)

    def __word_count(self, sentence):
        """If ordered=True, return OrderedDict object; if not standard dict"""
        # Split sentence
        word_list = sentence.split(" ")
        # Return dictionary
        dictionary = {}
        for w in word_list:
            word = w.lower().strip()
            # Manage in a single line both cases (present / not present)
            dictionary[word] = dictionary.get(word, 0)+1
            # v. 1.0 - Managed in more lines
            #if word in dictionary.keys():
            #    dictionary[word] += 1
            #else:
            #    dictionary[word] = 1
        # Remove not standard/unwanted keys
        if '' in dictionary.keys():
            del dictionary['']
        # Sort dictionary by values    
        if self.ordered:
            if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
                # Older Python
                print("WARNING: Python 3.6 or higher is required to have ordered dictionaries")
                print("You are using Python {}.{} and You'll get OrderedDict".format(sys.version_info.major, sys.version_info.minor))
                sorted_dictionary = OrderedDict(sorted(dictionary.items(), key=itemgetter(1), reverse=True))            
                return sorted_dictionary
            else: # Python 3.6
                sorted_dictionary = {k: v for k, v in sorted(dictionary.items(), key = lambda item: item[1], reverse=True)}
                return sorted_dictionary
        else:
            return dictionary

    def __file_reader(self):
        with open(self.file_name) as f: 
            data = f.read()
        return data
    
    def word_file_count(self):
        text = self.__file_reader()
        text = self.__clean(text)
        return self.__word_count(text)

def main():
    # Example of use of argparse 
    parser = argparse.ArgumentParser(description="File word counter")
    parser.add_argument('file_name', action="store")
    parser.add_argument('ordered', action="store", nargs="?", choices=['False', 'True'], default="False")
    args = parser.parse_args()

    if args.ordered == "False":
        wfc = WordFileCounter(args.file_name)
    else:
        wfc = WordFileCounter(args.file_name, True)
    print(wfc.word_file_count())

if __name__ == "__main__":
    main()