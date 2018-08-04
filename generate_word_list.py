import nltk
import string
import random
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

# Not used anymore
def find_after_in(corpus):
    """
    Finds interesting words that follow 'In', modified from:
    https://www.hallada.net/2017/07/11/generating-random-poems-with-python.html
    :param corpus: The corpus to look in broken into sentences
    :return:
    """
    # Find words after in
    corpus_words = corpus_list.sent(corpus)
    # Make bigrams (a list of two consecutive words)
    bigrams = [b for b in zip(corpus_words[:-1], corpus_words[1:])]

    # Make list of all words that follow 'in'
    condition = 'in'
    next_words = [bigram[1] for bigram in bigrams
                  if bigram[0].lower() == condition]

    # Only one of each word.
    next_words = list(set(next_words))

    # These are boring words, remove them & proper nouns
    forbid = ['my', 'its', 'an', 'a', 'and', 'the', 'at', 'to',
              'which', 'as', 'by', 'such', 'for', 'next', 'than', 'very',
              'their']
    next_words = [y for y in next_words if y[0].islower() and y not in forbid]

    # Break into two and one syl lists
    after_in_syls_1 = []
    after_in_syls_2 = []
    for x in next_words:
        if count_syllables(x) == 1:
            after_in_syls_1.append(x)
        elif count_syllables(x) == 2:
            after_in_syls_2.append(x)

    # Blank of Blank needs a two syllable noun noun
    corpus_sents =  corpus_list.sents(corpus)
    after_of_syls_2 = []
    for sent in corpus_sents:
        parsed_sent = nltk.pos_tag(sent)
        for word in parsed_sent:
            if word[1] in ['NN', 'NNS', 'VBG', 'DT', 'RBD'] and word[0] not in forbid and count_syllables(word[0])==2 and word[0].islower():
                after_of_syls_2.append(word[0])

    return after_in_syls_1, after_in_syls_2, after_of_syls_2


# Using this function
def generate_words_grammar():
    """
    Generates words based based on grammar parsing
    :param corpus: the text to pull from
    :return:
    """
    syls_1 = []
    syls_2 = []
    corpusdir = 'corpus'
    gentrification = PlaintextCorpusReader(corpusdir, '.*')
    gentrify_sents = gentrification.sents()
    wine_sents = nltk.corpus.webtext.sents('wine.txt')
    corpus_sents = gentrify_sents + wine_sents
    syls_1 = []
    syls_2 = []
    syls_4 = []

    for sent in corpus_sents:
        parsed_sent = nltk.pos_tag(sent)
        for word in parsed_sent:
            no_syls = count_syllables(word[0])
            if word[1] in ['NNS', 'JJ', 'NN']:
                if no_syls == 1:
                    syls_1 = syls_1 + [word[0]]
                elif no_syls == 2:
                    syls_2 = syls_2 + [word[0]]
                elif no_syls == 4:
                    syls_4 = syls_4+ [word[0]]
    return list(set(syls_1)), list(set(syls_2)), list(set(syls_4))

    # # Loop until we have 3 1 syllable words and 6 two syllable words
    #
    # while len(syls_2) < 6 or len(syls_1) < 3:
    #     # Pick a random sentence from the text and detect verbs, nouns etc.
    #     my_sent = random.choice(corpus_sents)
    #     parsed_sent = nltk.pos_tag(my_sent)
    #     for word in parsed_sent:
    #         # If noun, verb, determinant, not 'the' and more than 1 character long...
    #         if word[1] in ['NNS', 'JJ', 'NN'] and len(word[0]) > 1 \
    #                 and '*' not in word[0]:
    #             # Check the number of syllables, if 1 or 2 syllables, add to the list
    #             if len(syls_1) < 3 and count_syllables(word[0]) == 1:
    #                 # First 1 syllable word should not be a determinant, it sounds weird.
    #                 if len(syls_1) == 0:
    #                     syls_1.append(word[0].lower())
    #                     continue
    #                 syls_1.append(word[0].lower())
    #                 continue
    #             elif len(syls_2) < 6 and count_syllables(word[0]) == 2:
    #                 # Last 2 syllable word should be a noun (better mirrors "In cups of coffee")
    #                 syls_2.append(word[0].lower())
    #                 continue
    # # Put it all together
    # return syls_1, syls_2
