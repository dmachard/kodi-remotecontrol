from kodi_remotecontrol import Authenticator, Audio

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

# Basic audio controls
audio = Audio(session=sess)

# Select next audio track
audio.select_next()
