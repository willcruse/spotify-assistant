import sys
import os
sys.path.append("../spotify-interface/")

from SpotifyInterface import SpotifyInterface 
from time import sleep

si = SpotifyInterface()

si.nextSong()
sleep(3)
si.previousSong()