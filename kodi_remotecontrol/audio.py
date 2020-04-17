
from kodi_remotecontrol.eventclient import EventClient
from kodi_remotecontrol.httpclient import HttpClient

class Audio:
    def __init__(self, api_rc):
        """audio class"""
        self.api_rc = api_rc
        
    def select_next(self):
        """select next audio track"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Player.SetAudioStream",
                                 params={"playerid": 1, "stream": "next" })

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(AudioNextLanguage)")

    def current_audio(self):
        """get current audio"""   
        if isinstance(self.api_rc, HttpClient):     
            return self.api_rc.post(method="Player.GetProperties",
                                params={"playerid": 1, "properties": [ "currentaudiostream" ] })
                                                 
        if isinstance(self.api_rc, EventClient):
            return None
