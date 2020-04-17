from kodi_remotecontrol import HttpClient, Navigation

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = HttpClient(api_host=kodi_ip)

# Basic UI controls
nav = Navigation(api_rc=api_rc)

# Press on enter button
nav.press_enter()
