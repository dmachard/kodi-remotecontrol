from kodi_remotecontrol import HttpClient, Subtitle

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = HttpClient(api_host=kodi_ip)

# Basic subtitle controls
sub = Subtitle(api_rc=api_rc)

# Display subtitle
sub.press_on()
