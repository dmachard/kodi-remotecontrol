# Python client for Kodi Server API

![](https://github.com/dmachard/kodi_remotecontrol/workflows/Publish%20to%20PyPI/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dnsdist-console)

| | |
| ------------- | ------------- |
| Author |  Denis Machard <d.machard@gmail.com> |
| License |  MIT | 
| PyPI |  https://pypi.org/project/kodi-remotecontrol/ |
| | |

This is a Python remote control for Kodi Server through the **JSON-RPC HTTP** or the **Event Server** API
with minimal but sufficient basic controls.

## Table of contents
* [Installation](#installation)
* [Remote control](#remotre-control)
* [UI navigation](#ui-navigation)
* [Player interaction](#player-interaction)
* [Subtitle selection](#subtitle-selection)
* [Audio track selection](#audio-track-selection)

## Installation

```python
pip install kodi_remotecontrol
```

## Remote control

### HTTP client

As prerequisite, go to *System/Settings/Network/Services* and activate *Allow control of Kodi via HTTP*.

```python
from kodi_remotecontrol import HttpClient

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = HttpClient(api_host=kodi_ip)
```

### Event client

As prerequisite, go to 'System/Settings/Network/Services' and activate *Allow programs on other systems to control Kodi*.

```python
from kodi_remotecontrol import EventClient

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = EventClient(api_host=kodi_ip)
```

## UI navigation

```python
from kodi_remotecontrol import Navigation

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = EventClient(api_host=kodi_ip)

# ui navigation
nav = Navigation(api_rc=api_rc)
nav.press_enter()
```

| Buttons  |  Description |
|----------|--------------|
| press_up() | UP button |
| press_down() | DOWN button |
| press_left() | LEFT button |
| press_right() | RIGHT button |
| press_back() | BACK button |
| press_enter() | ENTER button |
| press_contextmenu() | CONTEXT MENU button |

## Player interaction

```python
from kodi_remotecontrol import Player

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = EventClient(api_host=kodi_ip)

# player interaction
nav = Player(api_rc=api_rc)
nav.press_play()
```

| Buttons  |  Description |
|----------|--------------|
| press_play() | PLAY button |
| press_stop() | STOP button |
| press_pause() | PAUSE button |
| press_shuffle() | SHUFFLE button |
| press_previous() | PREVIOUS button |
| press_next() | NEXT button |
| press_info() | INFO button |

## Subtitle selection

```python
from kodi_remotecontrol import Subtitle

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = EventClient(api_host=kodi_ip)

# subtitle selection
sub = Subtitle(api_rc=api_rc)
sub.press_show()
```

| Buttons  |  Description |
|----------|--------------|
| press_show() | SHOW button |
| select_next() | NEXT button |

## Audio track selection

```python
from kodi_remotecontrol import Audio

# prepare remote control
kodi_ip = "10.0.0.200"
api_rc = EventClient(api_host=kodi_ip)

# audio track selection
aud = Audio(api_rc=api_rc)
aud.select_next()
```

| Buttons  |  Description |
|----------|--------------|
| select_next() | NEXT button |
