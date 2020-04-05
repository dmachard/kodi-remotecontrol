from kodi_remotecontrol import Authenticator, Navigation

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

# Basic controls
nav = Navigation(session=sess)
print(nav.press_up())
#{'id': 1, 'jsonrpc': '2.0', 'result': 'OK'}

# nav.press_up()
# nav.press_down()
# nav.press_left()
# nav.press_right()
# nav.press_back()
# nav.press_enter()
# nav.press_contextmenu()