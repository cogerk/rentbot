import nltk
import string
import random

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


def find_after_in(corpus, corpus_list):
    """
    Finds interesting words that follow 'In', modified from:
    https://www.hallada.net/2017/07/11/generating-random-poems-with-python.html
    :param corpus: The corpus to look in
    :return:
    """
    # Find words after in
    corpus_list =eval(corpus_list)
    corpus_words = corpus_list.words(corpus)
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


# Not using this function
def generate_words_grammar(corpus='wine.txt'):
    """
    Generates words based based on grammar parsing
    :param corpus: the text to pull from
    :return:
    """
    syls_1 = []
    syls_2 = []
    # Loop until we have 3 1 syllable words and 6 two syllable words
    while len(syls_2) < 6 or len(syls_1) < 3:
        # Pick a random sentence from the text and detect verbs, nouns etc.
        corpus_sents = nltk.corpus.webtext.sents(corpus)
        my_sent = random.choice(corpus_sents)
        parsed_sent = nltk.pos_tag(my_sent)
        for word in parsed_sent:
            # If noun, verb, determinant, not 'the' and more than 1 character long...
            if word[1] in ['NN', 'NNS', 'VBG', 'DT', 'RBD'] and word[0].lower() != 'the' and len(word[0]) > 1 \
                    and '*' not in word[0]:
                # Check the number of syllables, if 1 or 2 syllables, add to the list
                if len(syls_1) < 3 and count_syllables(word[0]) == 1:
                    # First 1 syllable word should not be a determinant, it sounds weird.
                    if len(syls_1) == 0 and word[1] is not 'DT':
                        syls_1.append(word[0].lower())
                        continue
                    syls_1.append(word[0].lower())
                    continue
                elif len(syls_2) < 6 and count_syllables(word[0]) == 2:
                    # Last 2 syllable word should be a noun (better mirrors "In cups of coffee")
                    if len(syls_2) == 5 and word[1] in ['NN', 'NNS']:
                        syls_2.append(word[0].lower())
                        continue
                    syls_2.append(word[0].lower())
                    continue
    # Put it all together
    return syls_1, syls_2
