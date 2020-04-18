# Python remote control for Kodi

![](https://github.com/dmachard/kodi_remotecontrol/workflows/Publish%20to%20PyPI/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dnsdist-console)

| | |
| ------------- | ------------- |
| Author |  Denis Machard <d.machard@gmail.com> |
| License |  MIT | 
| PyPI |  https://pypi.org/project/kodi-remotecontrol/ |
| | |

This is a Python remote control for Kodi with minimal but sufficient basic controls.

This remote control acts as a websocket proxy of the **Event Server** API for more reactivity.

## Table of contents
* [Installation](#installation)
* [Start remote control](#start-remote-control)
* [Available buttons](#available-buttons)

## Installation

```python
pip install kodi_remotecontrol
```

## Start remote control

As prerequisite, go to `System/Settings/Network/Services` and activate `Allow programs on other systems to control Kodi`.
After that, you can start the remote control and provides the address of your kodi server.

```
kodi_remotecontrol --desthost=10.0.0.200
```

Other available options:

```
kodi_remotecontrol --help
usage: kodi_remotecontrol [-h] [--destport DESTPORT] [--desthost DESTHOST]
                        [--bindport BINDPORT] [--bindhost BINDHOST]

optional arguments:
  -h, --help           show this help message and exit
  --destport DESTPORT  destination kodi port default=9777
  --desthost DESTHOST  destination kodi host default=127.0.0.1
  --bindport BINDPORT  bind on port default=8081
  --bindhost BINDHOST  bind on host default=0.0.0.0
```

## Available buttons

To interact with the remote control, you need to use a websocket client and 
send the following **JSON** commands to the address `ws://<remotecontrol_ip>:8081`.

### UI Navigation

| Commands |  Description |
|----------|--------------|
| {'button': 'press_up'} | press on up button |
| {'button': 'press_down'} | press on down button |
| {'button': 'press_left'} | press on left button |
| {'button': 'press_right'} | press on right button |
| {'button': 'press_back'} | press on back button |
| {'button': 'press_enter'} | press on enter button |
| {'button': 'press_ctxmenu'} | display contextual menu |
| {'button': 'press_playlist'} | display playlist |
| {'button': 'press_logoff'} | press on logoff button |

### Player interaction

| Commands  |  Description |
|----------|--------------|
| {'button': 'press_play'} | press on play button |
| {'button': 'press_stop'} | press on stop button |
| {'button': 'press_pause'} | press on pause button |
| {'button': 'press_previous'}| press on previous button |
| {'button': 'press_next'} | press on next button |
| {'button': 'press_osd'} | display OSD |

### Subtitle selection

| Commands  |  Description |
|----------|--------------|
| {'button': 'press_subtitle'} | Toggle subtitle |

### Audio track selection

| Commands  |  Description |
|----------|--------------|
| {'button': 'press_language'} | Toggle language |
