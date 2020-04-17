from kodi_remotecontrol import HttpClient, Audio

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = HttpClient(api_host=kodi_ip)

# Basic audio controls
audio = Audio(api_rc=api_rc)

# Select next audio track
audio.select_next()
