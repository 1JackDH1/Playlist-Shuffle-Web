''' Implementation for random shuffling of playlist items '''

# pylint: disable=W0718

from random import shuffle

def random_shuffle(shuffle_list):
    ''' Simple function for in-place shuffling,
    random shuffle implements the Fisher-Yates shuffle'''
    try:
        shuffle(shuffle_list)
    except Exception as e:
        print(e)
    return shuffle_list
