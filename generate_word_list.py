import nltk
import string
import random

# Download relevant corpuses
nltk.download('cmudict')
nltk.download('webtext')
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
print('test body')

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
    corpus_sents = corpus_list.sents(corpus)
    after_of_syls_2 = []
    for sent in corpus_sents:
        parsed_sent = nltk.pos_tag(sent)
        for word in parsed_sent:
            if word[1] in ['NN', 'NNS', 'VBG', 'DT', 'RBD'] and word[0] not in forbid and count_syllables(word[0])==2 and word[0].islower():
                after_of_syls_2.append(word[0])

    return after_in_syls_1, after_in_syls_2, after_of_syls_2

# Corpuses to search
text_files = ['wine.txt', 'overheard.txt', 'singles.txt']

# for each file, concatenate lists of 1 syl. & 2 syl. words following in as well as list of nouns
syls_1 = []
syls_2 = []
of_syls_2 = []
for file in text_files:
    words = find_after_in(corpus=file, corpus_list=nltk.corpus.webtext)
    syls_1 = list(set(syls_1 + words[0]))
    syls_2 = list(set(syls_2 + words[1]))
    of_syls_2 = list(set(of_syls_2 + words[2]))


# Not quite enough  1 syl. & 2 syl. words, so we'll supplement a few more corpuses
words1 = find_after_in(corpus='bible-kjv.txt', corpus_list=nltk.corpus.gutenberg)
words2 = find_after_in(corpus='carroll-alice.txt', corpus_list=nltk.corpus.gutenberg)

syls_1 = list(set(syls_1 + random.choices(words1[0], k=50) + words2[0]))
syls_2 = list(set(syls_2 + random.choices(words2[1], k=40) + words2[1]))