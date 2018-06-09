# imports
import random
from words_vars import *


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
