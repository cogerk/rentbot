from generate_word_list import generate_words_grammar

# Find all the words that could be used at rent lyrics
syls_1, syls_2, syls_4, syls_2_sing = generate_words_grammar()

# Save all word lists in separate file
f = open('words_vars.py', 'w')
f.write('syls_1 = ' + repr(syls_1) + '\n')
f.write('syls_2 = ' + repr(syls_2) + '\n')
f.write('syls_2_sing = ' + repr(syls_2_sing) + '\n' )
f.write('syls_4 = ' + repr(syls_4) + '\n' )
f.close()
