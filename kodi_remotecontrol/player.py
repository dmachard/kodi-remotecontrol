
from kodi_remotecontrol.eventclient import EventClient
from kodi_remotecontrol.httpclient import HttpClient

class Player:
    def __init__(self, api_rc):
        """player class"""
        self.api_rc = api_rc
        
    def press_play(self):
        """press on play button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Player.PlayPause",
                                         params={"playerid": 1, "play": True})

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Play)")

    def press_pause(self):
        """press on pause button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Player.PlayPause",
                                         params={"playerid": 1, "play": False})

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Pause)")

    def press_stop(self):
        """press on stop button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Player.Stop",
                                         params={"playerid": 1})

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Stop)")

    def press_shuffle(self):
        """press on random button"""
        if isinstance(self.api_rc, HttpClient):   
            r = self.api_rc.post(method="Player.GetProperties",
                                      params={"playerid": 1, "properties": [ "shuffled" ]})
            if r["result"]["shuffled"]:
                return self.api_rc.post(method="Player.SetShuffle",
                                             params={"playerid": 1, "shuffle": False})
            else:
                return self.api_rc.post(method="Player.SetShuffle",
                                             params={"playerid": 1, "shuffle": True})
        
        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(RandomPreset)")

    def press_previous(self):
        """press on previous button"""
        if isinstance(self.api_rc, HttpClient):   
            self.api_rc.post(method="Player.GoTo",
                                  params={"playerid": 1,
                                          "to": "previous"})
        
        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(SkipPrevious)")

    def press_next(self):
        """press on next button"""
        if isinstance(self.api_rc, HttpClient):   
            self.api_rc.post(method="Player.GoTo",
                                  params={"playerid": 1,
                                          "to": "next"})
        
        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(SkipNext)")

    def press_info(self):
        """press on info (osd) button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Input.ShowOSD")

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(OSD)")
