from kodi_remotecontrol import Authenticator, Subtitle

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

sub = Subtitle(session=sess)
print(sub.press_on())
# {'id': 1, 'jsonrpc': '2.0', 'result': 'OK'}

# sub.press_on()
# sub.press_off()
# sub.select_next()
# sub.select_previous()
