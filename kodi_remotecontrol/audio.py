
class Audio:
    def __init__(self, session):
        """audio class"""
        self.sess = session
        
    def select_next(self):
        """select next audio track"""
        self.sess.post(method="Player.SetAudioStream",
                       params={"playerid": 1, "stream": "next" })
                       
        return self.sess.post(method="Player.GetProperties",
                              params={"playerid": 1, 
                                      "properties": [ "currentaudiostream" ] })
                              
    def select_previous(self):
        """select previous audio track"""
        self.sess.post(method="Player.SetAudioStream",
                       params={"playerid": 1, "stream": "previous" })
        
        return self.sess.post(method="Player.GetProperties",
                              params={"playerid": 1, 
                                      "properties": [ "currentaudiostream" ] })