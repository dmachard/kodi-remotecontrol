
class Subtitle:
    def __init__(self, session):
        """subtitle class"""
        self.sess = session
        
    def select_next(self):
        """select next subtitle"""
        self.sess.post(method="Player.SetSubtitle",
                              params={"playerid": 1, "subtitle": "next" })
                              
        return self.sess.post(method="Player.GetProperties",
                              params={"playerid": 1, 
                                      "properties": [ "currentsubtitle" ] })
                              
    def select_previous(self):
        """select previous subtitle"""
        self.sess.post(method="Player.SetSubtitle",
                              params={"playerid": 1, "subtitle": "previous" })
                              
        return self.sess.post(method="Player.GetProperties",
                              params={"playerid": 1, 
                                      "properties": [ "currentsubtitle" ] })
            
    def press_on(self):
        """play the current subtitle"""
        return self.sess.post(method="Player.SetSubtitle",
                              params={"playerid": 1, subtitle: "on"})
        
    def press_off(self):
        """stop to play subtitle"""
        return self.sess.post(method="Player.SetSubtitle",
                              params={"playerid": 1, subtitle: "off"})