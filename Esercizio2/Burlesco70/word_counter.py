import re # To do text cleaning
import sys # To check Python version
import argparse # To manage args
import chardet # To guess encoding
# To create world cloud image
from wordcloud import WordCloud
import numpy as np
from PIL import Image

if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
    # WARNING: Python 3.6 or higher is required to have ordered dictionaries
    from operator import itemgetter
    from collections import OrderedDict

def make_image(freq_dict, mask_file = 'famiglia.png', word_cloud_file = 'word_counter.png'):
    """WorldCloud image creator"""
    image_mask = np.array(Image.open(mask_file))
    wc = WordCloud(background_color="white", max_words=1000, 
                   mask=image_mask, contour_width=3, contour_color='firebrick')
    # generate word cloud
    wc.generate_from_frequencies(freq_dict)
    # write image file
    print("Wordcloud file: ", word_cloud_file)
    wc.to_file(word_cloud_file)

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
        # Guess file encoding with chardet
        with open(self.file_name, "rb") as rawdata:
            rawtext = rawdata.read()
        enco = chardet.detect(rawtext)['encoding']
        # Open with guessed encoding
        with open(self.file_name, encoding = enco) as f: 
            data = f.read()
        return data
    
    def word_file_count(self):
        text = self.__file_reader()
        text = self.__clean(text)
        dict_result = self.__word_count(text)        
        make_image(dict_result)
        return dict_result

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
    print("Dictionary with word frequencies: ", wfc.word_file_count())

if __name__ == "__main__":
    main()