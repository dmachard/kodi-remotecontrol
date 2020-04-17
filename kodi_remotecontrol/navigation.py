
from kodi_remotecontrol.eventclient import EventClient
from kodi_remotecontrol.httpclient import HttpClient

class Navigation:
    def __init__(self, api_rc):
        """navigation class"""
        self.api_rc = api_rc
        
    def press_left(self):
        """press on left button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Input.Left")
        
        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Left)")

    def press_right(self):
        """press on right button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Input.Right")

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Right)")

    def press_up(self):
        """press on up button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Input.Up") 
            
        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Left)")

    def press_down(self):
        """press down button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Input.Down")

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Down)")

    def press_enter(self):
        """press on enter button"""
        if isinstance(self.api_rc, JsonAPI):
            self.api_rc.post(method="Input.Select")

        if isinstance(self.api_rc, EventAPI):
            self.api_rc.send_action(msg="Action(Select)")

    def press_back(self):
        """press on back button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Input.Back")

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(Back)")

    def press_contextmenu(self):
        """press on menu button"""
        if isinstance(self.api_rc, HttpClient):
            self.api_rc.post(method="Input.ContextMenu")

        if isinstance(self.api_rc, EventClient):
            self.api_rc.send_action(msg="Action(ContextMenu)")