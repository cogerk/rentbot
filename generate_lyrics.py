# imports
import random
from words_vars import * # List of words saved by save_word_list


def generate_lyrics():
    """
    Generates rent lyrics from a previously saved list of words saved in word_vars.py
    :return:
    """
    # Line 4 can have either 1 long word or two short words on
    # 33% chance that it's just one long word
    format_choice = random.choice([0, 1, 2])
    if format_choice == 2:
        rand_syls_1 = random.choices(syls_1, k=2)
        rand_syls_2 = random.choices(syls_2, k=5)
        rand_syls_4 = random.choices(syls_4, k=1)
        return ('How do you measure? Measure a year?\n' +
                'In ' + rand_syls_2[0] + ',\n' +
                'In ' + rand_syls_2[1] + ',\n' +
                'In ' + rand_syls_2[2] + ',\n' +
                'In ' + rand_syls_4[0] + '.\n\n' +
                'In ' + rand_syls_2[3] + ', in ' + rand_syls_1[0] + ', in ' +
                rand_syls_2[4] + ', in ' + rand_syls_1[1] + '.')
    else:
        rand_syls_1 = random.choices(syls_1, k=3)
        rand_syls_2 = random.choices(syls_2, k=5)
        rand_syls_2_sing = random.choices(syls_2_sing+syls_2)
        return ('How do you measure? Measure a year?\n' +
                'In ' + rand_syls_2[0] + ',\n' +
                'In ' + rand_syls_2[1] + ',\n' +
                'In ' + rand_syls_2[2] + ',\n' +
                'In ' + rand_syls_1[0] + ' of ' + rand_syls_2_sing[0]  + '.\n\n' +
                'In ' + rand_syls_2[3] + ', in ' + rand_syls_1[1] + ', in ' +
                rand_syls_2[4] + ', in ' + rand_syls_1[2] + '.')
