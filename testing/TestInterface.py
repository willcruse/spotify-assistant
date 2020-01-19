import sys
sys.path.append("../spotify-interface/")

from SpotifyInterface import SpotifyInterface 
from time import sleep

si = SpotifyInterface("zsfhjrarbgsz8595eqt4l6zxp")

si.nextSong()
sleep(3)
si.previousSong()