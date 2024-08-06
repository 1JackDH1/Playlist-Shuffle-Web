''' Main program file '''

import playlist
import playlistitems
from shuffle import random_shuffle

def main():
    ''' Main function, consolidation of other Python scripts. '''
    playlist_ids = playlist.get_playlist()
    print("All playlists in account:")
    for list_id in playlist_ids:
        print(list_id + '\n')

    video_id_list = playlistitems.get_playlist_items()
    shuffled_list = random_shuffle(video_id_list)
    print(len(shuffled_list))


if __name__ == "__main__":
    main()
