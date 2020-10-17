#!/bin/sh

# start the program
python -c "from kodi_remotecontrol import gateway; gateway.start_remotecontrol()" --desthost $KODI_HOST --destport $KODI_PORT