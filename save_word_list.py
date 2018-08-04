import random
from generate_word_list import generate_words_grammar

# Deprecated
# # Corpuses to search
# text_files = ['wine.txt', 'overheard.txt', 'singles.txt']
# # for each file, concatenate lists of 1 syl. & 2 syl. words following in as well as list of nouns
# syls_1 = []
# syls_2 = []
# of_syls_2 = []
# for file in text_files:
#     words = find_after_in(corpus=file, corpus_list='nltk.corpus.webtext')
#     syls_1 = list(set(syls_1 + words[0]))
#     syls_2 = list(set(syls_2 + words[1]))
#     of_syls_2 = list(set(of_syls_2 + words[2]))
# # Not quite enough  1 syl. & 2 syl. words, so we'll supplement a few more corpuses
# words1 = find_after_in(corpus='bible-kjv.txt', corpus_list='nltk.corpus.gutenberg')
# words2 = find_after_in(corpus='carroll-alice.txt', corpus_list='nltk.corpus.gutenberg')
syls_1, syls_2, syls_4, syls_2_sing = generate_words_grammar()


f = open('words_vars.py', 'w')
f.write('syls_1 = ' + repr(syls_1) + '\n')
f.write('syls_2 = ' + repr(syls_2) + '\n')
f.write('syls_2_sing = ' + repr(syls_2_sing) + '\n' )
f.write('syls_4 = ' + repr(syls_4) + '\n' )
f.close()
