
class Player:
    def __init__(self, session):
        """player class"""
        self.sess = session
        
    def press_play(self):
        """press on play button"""
        return self.sess.post(method="Player.PlayPause",
                              params={"playerid": 1, "play": True})
        
    def press_pause(self):
        """press on pause button"""
        return self.sess.post(method="Player.PlayPause",
                              params={"playerid": 1, "play": False})
        
    def press_stop(self):
        """press on stop button"""
        return self.sess.post(method="Player.Stop",
                              params={"playerid": 1})
        
    def press_shuffle(self):
        """press on random button"""
        r = self.sess.post(method="Player.GetProperties",
                           params={"playerid": 1, "properties": [ "shuffled" ]})
        if r["result"]["shuffled"]:
            return self.sess.post(method="Player.SetShuffle",
                                  params={"playerid": 1, "shuffle": False})
        else:
            return self.sess.post(method="Player.SetShuffle",
                                  params={"playerid": 1, "shuffle": True})
        
    def press_previous(self):
        """press on previous button"""
        return self.sess.post(method="Player.GoTo",
                              params={"playerid": 1,
                                      "to": "previous"})
        
    def press_next(self):
        """press on next button"""
        return self.sess.post(method="Player.GoTo",
                              params={"playerid": 1,
                                      "to": "next"})
         
    def press_info(self):
        """press on info (osd) button"""
        return self.sess.post(method="Input.ShowOSD")   
