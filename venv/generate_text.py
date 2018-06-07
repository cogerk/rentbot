# imports
import string
import random
import nltk

# import source material
text = nltk.corpus.webtext.sents('wine.txt')
cmu = nltk.corpus.cmudict.dict()

def count_syllables(word):
    lower_word = word.lower()
    if lower_word in cmu:
        return max([len([y for y in x if y[-1] in string.digits])
                    for x in cmu[lower_word]])



syls_1 = []
syls_2 = []
while (len(syls_2)<6 or len(syls_1)<3):
    my_sent = random.choice(text)
    parsed_sent = nltk.pos_tag(my_sent)

    for word in parsed_sent:
        if word[1] in ['NN', 'NNS', 'VBG', 'DT', 'RBD'] and word[0].lower() is not 'the' and len(word[0])>1 and '*' not in word[0]:
            print(word)
            if len(syls_1)<3 and count_syllables(word[0]) == 1:
                if len(syls_1)==0 and word[1] is not 'DT':
                    syls_1.append(word[0].lower())
                    continue
                syls_1.append(word[0].lower())
                continue
            elif len(syls_2)<6 and count_syllables(word[0]) == 2:
                if len(syls_2)==5 and word[1] in ['NN', 'NNS']:
                    syls_2.append(word[0].lower())
                    continue
                syls_2.append(word[0].lower())
                continue


# Put it all together
print('How do you measure? Measure a year?')
print('In ' +syls_2[0] +',\n' +
      'In ' +syls_2[1] +',\n' +
      'In ' +syls_2[2] +',\n' +
      'In ' +syls_1[0] +' of ' + syls_2[3] +'.\n\n' +
      'In '+syls_2[4] +', in ' + syls_1[1] + ', in ' + syls_2[5] + ', in ' + syls_1[2] +'.')

