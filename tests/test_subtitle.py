from kodi_remotecontrol import Authenticator, Subtitle

# ip remote server
ip_kodi = "10.0.0.200"

# Authenticator
sess = Authenticator(api_host=ip_kodi)

# Basic subtitle controls
sub = Subtitle(session=sess)

# Display subtitle
sub.press_on()
