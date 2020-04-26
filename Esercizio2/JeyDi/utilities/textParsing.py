import nltk
import spacy
import re
from tqdm import tqdm
from spacy_langdetect import LanguageDetector

# WARNING you need to download this model before if you have some errors by doing for example:
# python -m spacy download en_core_web_sm
try:
    NLP_it = spacy.load('it_core_news_sm', parse=True, tag=True, entity=True)
    NLP_en = spacy.load('en_core_web_sm', parse=True, tag=True, entity=True)
    NLP_dect = spacy.load('en')

except Exception as message:
    print(f"WARNING! You have to download the language model first: {message}")


def simple_parse(input_text):
    """
    Parse the input text with a simple regexp
    :param input_text: the text you want to parse and count
    :return: cleaned text
    """
    try:
        text = re.sub(r'[^A-Za-z ]+', r' ', input_text, flags=re.MULTILINE)
        text_result = text.lower().strip()
        return text_result
    except Exception as message:
        print(f"Error parsing the requested text: {message}")
        return ''


def count_words(input_text, sort=True):
    """
    Count the words in the text and get a dictionary with word relative frequency
    :return:
    """
    result = {}
    input_text = input_text.split()
    try:
        for words in tqdm(input_text):
            result[words] = input_text.count(words)

        if sort:
            print("Sorting the dictionary")
            result = {key: text for key, text in sorted(result.items(), key=lambda item: item[1], reverse=True)}

        unique_words = len(result)
        total_words = len(input_text)

        print(f"Total number of words: {total_words}")
        print(f"Unique number of words: {unique_words}")

        return result

    except Exception as message:
        print(f"Error, impossible count the words: {message}")
        return None


def check_language(input_text):
    """
    Check the language of an input text
    :param input_text:
    :return: the name of the language
    """
    NLP_dect.add_pipe(LanguageDetector(), name='language_detector', last=True)
    language = NLP_dect(input_text)._.language
    print(f"Text language: {language}")

    return language['language']


def tokenization(input_text, language, stemming=True):
    """
    Italian Tokenization using NLTK Corpus and Stemmers
    Need to be applied to a single text, so at every row in a dataframe (using Apply)
    :param text: a single row with input text
    :return: processed text
    """
    print("Executing Tokenization...")
    # Check the language
    # Italian language
    if language == 'it':
        print(f"You are using: {language} language")
        # dictionary of Italian stop-words
        stop_words = nltk.corpus.stopwords.words('italian')
        # Snowball stemmer with rules for the Italian language
        stemmer = nltk.stem.snowball.ItalianStemmer(ignore_stopwords=True)

    # English language
    elif language == 'en':
        print(f"You are using: {language} language")
        # dictionary of English stop-words
        stop_words = nltk.corpus.stopwords.words('english')
        # Snowball stemmer with rules for the English language
        stemmer = nltk.stem.snowball.EnglishStemmer(ignore_stopwords=True)
    else:
        print(f"You are using: {language} language")
        print("Sorry, the language of the file is unknown...please check the input file or the code..")
        return None

    tokens = nltk.word_tokenize(input_text)

    # Tokenize
    tokens = [token.strip() for token in tokens]

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    if stemming:
        # Stem
        tokens = [stemmer.stem(token) for token in tokens]

    # Reconstruct the text
    token_result = ' '.join([token for token in tokens])

    return token_result


def lemmatize(input_text, language):
    """
    Lemmatize words using NLP Spacy package
    :param nlp: Spacy NLP function
    :param text: Text to lemmatize
    :return: List of words lemmatized
    """
    print("Executing Lemmatization...")
    # Check the language to identify wich NLP model you have to use
    if language == 'it':
        print(f"You are using: {language} language")
        nlp_active = NLP_it
    elif language == 'en':
        print(f"You are using: {language} language")
        nlp_active = NLP_en
    else:
        print(f"You are using: {language} language")
        print("Sorry, the language of the file is unknown...please check the input file or the code..")
        return None

    # Apply lemmatization
    text = nlp_active(input_text)
    result = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])

    return result


def old_count_words(input_text):
    """
    Count the number fo words in a text
    :param input_text: input text with words
    :return: number of words
    """
    n_words = {lambda x: len(x.split(' ')).sum()}

    print('Number of words', n_words)

    return n_words
