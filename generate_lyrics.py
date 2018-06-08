# imports
import random
import nltk
from generate_word_list import syls_1, syls_2, of_syls_2, count_syllables


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


def generate_lyrics():
    rand_syls_1 = random.choices(syls_1, k=3)
    rand_syls_2 = random.choices(syls_2, k=5)
    rand_of_syls_2 = random.choice(of_syls_2)
    return ('How do you measure? Measure a year?\n' +
            'In ' + rand_syls_2[0] + ',\n' +
            'In ' + rand_syls_2[1] + ',\n' +
            'In ' + rand_syls_2[2] + ',\n' +
            'In ' + rand_syls_1[0] + ' of ' + rand_of_syls_2 + '.\n\n' +
            'In ' + rand_syls_2[3] + ', in ' + rand_syls_1[1] + ', in ' +
            rand_syls_2[4] + ', in ' + rand_syls_1[2] + '.')
