from __future__ import print_function
import sys
import spotipy
import spotipy.util as util



# username = "zsfhjrarbgsz8595eqt4l6zxp"

class SpotifyInterface:

    def __init__(self, username):
        scope = 'user-read-playback-state streaming'
        self.token = util.prompt_for_user_token(username, scope)
        self.scope = 'user-read-playback-state streaming'
        if self.token:
            self.sp = spotipy.Spotify(auth=self.token)
        else:
            raise Exception("Could not fetch token")

    def getCurrentTrack(self):
        curr = self.sp.current_playback()
        artists = curr.get("item", {}).get("album", {}).get("artists", {})
        if len(artists) > 0:
            return {
                "title": curr.get("item", {}).get("name", ""), 
                "artist": artists[0].get("name", None)
            }
        else:
            return None
    
    def pausePlayback(self):
        self.sp.pause_playback()
    
    def playPlayback(self):
        self.sp.start_playback()

    def nextSong(self):
        self.sp.next_track()
    
    def previousSong(self):
        self.sp.previous_track()
    
    