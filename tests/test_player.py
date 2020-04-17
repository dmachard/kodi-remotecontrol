from kodi_remotecontrol import HttpClient, Player

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = HttpClient(api_host=kodi_ip)

# Basic player controls
player = Player(api_rc=api_rc)

# Press on play button
player.press_play()