from kodi_remotecontrol import Authenticator, Player

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

# Basic player controls
player = Player(session=sess)

# Press on play button
player.press_play()