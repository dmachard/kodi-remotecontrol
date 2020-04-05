from kodi_remotecontrol import Authenticator, Player

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

player = Player(session=sess)
print(player.press_shuffle())
# {'id': 1, 'jsonrpc': '2.0', 'result': 'OK'}

# player.press_play()
# player.press_stop()
# player.press_pause()
# player.press_shuffle()
# player.press_previous()
# player.press_next()
# player.press_info()