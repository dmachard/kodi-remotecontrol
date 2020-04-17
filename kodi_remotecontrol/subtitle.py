
from kodi_remotecontrol.eventclient import EventClient
from kodi_remotecontrol.httpclient import HttpClient

class Subtitle:
    def __init__(self, api_rc):
        """subtitle class"""
        self.api_rc = api_rc
        
    def select_next(self):
        """select next subtitle"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Player.SetSubtitle",
                                  params={"playerid": 1, "subtitle": "next" })

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(NextSubtitle)")

    def current_subtitle(self):
        """get current subtitle"""
        if isinstance(self.api_rc, JsonAPI):                 
            return self.api_rc.post(method="Player.GetProperties",
                                         params={"playerid": 1, 
                                                "properties": [ "currentsubtitle" ] })

        if isinstance(self.api_rc, EventAPI):
            return None
        
    def press_show(self):
        """toggle subtitle"""
        if isinstance(self.api_rc, HttpClient):
            r = self.api_rc.post(method="Player.GetProperties",
                                  params={"playerid": 1, "properties": [ "subtitleenabled" ]})
            if r["result"]["subtitleenabled"]:
                self.api_rc.post(method="Player.SetSubtitle",
                                      params={"playerid": 1, "subtitle": "off"})
            else:
                self.api_rc.post(method="Player.SetSubtitle",
                                      params={"playerid": 1, "subtitle": "on"})

        if isinstance(self.api_rc, EventAPI):
            self.api_rc.send_action(msg="Action(ShowSubtitles)")
