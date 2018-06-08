# imports
import string
import random
import nltk

# Import source material & dictionary
text = nltk.corpus.webtext.sents('wine.txt')
cmu = nltk.corpus.cmudict.dict()


# Syllable counting function
# Stolen from:
def count_syllables(word):
    lower_word = word.lower()
    if lower_word in cmu:
        return max([len([y for y in x if y[-1] in string.digits])
                    for x in cmu[lower_word]])


# Generate the text
def generate_lyrics(corpus=text):
    syls_1 = []
    syls_2 = []
    # Loop until we have 3 1 syllable words and 6 two syllable words
    while len(syls_2) < 6 or len(syls_1) < 3:
        # Pick a random sentence from the text and detect verbs, nouns etc.
        my_sent = random.choice(corpus)
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
    return('How do you measure? Measure a year?\n' +
           'In ' + syls_2[0] + ',\n' +
           'In ' + syls_2[1] + ',\n' +
           'In ' + syls_2[2] + ',\n' +
           'In ' + syls_1[0] + ' of ' + syls_2[3] + '.\n\n' +
           'In ' + syls_2[4] + ', in ' + syls_1[1] + ', in ' + syls_2[5] + ', in ' + syls_1[2] + '.')
