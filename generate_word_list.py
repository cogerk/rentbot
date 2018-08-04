import nltk
import string
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

# Download relevant corpuses
nltk.download('cmudict')
nltk.download('webtext')
nltk.download('gutenberg')
cmu = nltk.corpus.cmudict.dict()


def count_syllables(word):
    """
    # Syllable counting function
    # Stolen from: https://www.hallada.net/2017/07/11/generating-random-poems-with-python.html
    :param word: word to count syllables in
    :return:
    """
    lower_word = word.lower()
    if lower_word in cmu:
        return max([len([y for y in x if y[-1] in string.digits])
                    for x in cmu[lower_word]])


def generate_words_grammar():
    """
    Use sentence grammar to find words that could be Rent lyrics
    :return:
    """
    # Load corpuses to look in
    gentrification = PlaintextCorpusReader('corpus', '.*')  # Gentrification articles are in this directory
    gentrify_sents = gentrification.sents()  #
    wine_sents = nltk.corpus.webtext.sents('wine.txt')
    corpus_sents = gentrify_sents + wine_sents
    syls_1 = []
    syls_2 = []
    syls_4 = []
    syls_2_sing = []
    for sent in corpus_sents:
        parsed_sent = nltk.pos_tag(sent)
        for word in parsed_sent:
            no_syls = count_syllables(word[0])
            if word[1] == 'NNS' and len(word[0]) > 3:
                if no_syls == 1:
                    syls_1 = syls_1 + [word[0].lower()]
                elif no_syls == 2:
                    syls_2 = syls_2 + [word[0].lower()]
                elif no_syls == 4:
                    syls_4 = syls_4 + [word[0].lower()]
            if word[1] == 'NN' and len(word[0]) > 2:
                if no_syls == 2:
                    syls_2_sing = syls_2_sing + [word[0].lower()]
    return list(set(syls_1)), list(set(syls_2)), list(set(syls_4)), list(set(syls_2_sing))
