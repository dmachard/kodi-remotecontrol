from kodi_remotecontrol import Authenticator, Audio

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

audio = Audio(session=sess)
print(audio.select_next())
# {'id': 1, 'jsonrpc': '2.0', 'result': 'OK'}

# audio.select_next()
# audio.select_previous()
