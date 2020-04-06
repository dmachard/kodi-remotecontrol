from kodi_remotecontrol import Authenticator, Navigation

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

# Basic UI controls
nav = Navigation(session=sess)

# Press on enter button
nav.press_enter()
