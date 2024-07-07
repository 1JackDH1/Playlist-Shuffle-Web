''' Main program file '''

import playlistitems
from shuffle import random_shuffle

if __name__ == "__main__":
    full_list = playlistitems.get_playlist_items()
    shuffled_list = random_shuffle(full_list)
    print(len(shuffled_list))
    print(shuffled_list[0])
    print(shuffled_list[-1])
