
class Navigation:
    def __init__(self, session):
        """navigation class"""
        self.sess = session
        
    def press_left(self):
        """press on left button"""
        return self.sess.post(method="Input.Left")

    def press_right(self):
        """press on right button"""
        return self.sess.post(method="Input.Right")

    def press_up(self):
        """press on up button"""
        return self.sess.post(method="Input.Up")  

    def press_down(self):
        """press down button"""
        r = self.sess.post(method="Input.Down")
        return r["result"]  

    def press_enter(self):
        """press on enter button"""
        return self.sess.post(method="Input.Select")

    def press_back(self):
        """press on back button"""
        return self.sess.post(method="Input.Back")

    def press_contextmenu(self):
        """press on menu button"""
        return self.sess.post(method="Input.ContextMenu")
