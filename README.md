# Python client for Kodi Server

![](https://github.com/dmachard/kodi_remotecontrol/workflows/Publish%20to%20PyPI/badge.svg)

| | |
| ------------- | ------------- |
| Author |  Denis Machard <d.machard@gmail.com> |
| License |  MIT | 
| PyPI |  https://pypi.org/project/kodi-remotecontrol/ |
| | |

This is a Python remote control for Kodi Server through the REST API 
with the minimal but sufficient basic controls.

## Table of contents
* [Installation](#installation)
* [Authentication](#authentication)
* [UI navigation](#ui-navigation)
* [Player interaction](#player-interaction)
* [Subtitle selection](#subtitle-selection)
* [Audio track selection](#audio-track-selection)

## Installation

```python
pip install kodi_remotecontrol
```

## Authentication

```python
from kodi_remotecontrol import Authenticator

kodi_ip = "10.0.0.240"
session = Authenticator(api_host=kodi_ip)
```
 
## UI navigation

```python
from kodi_remotecontrol import Navigation

nav = Navigation(session=session)

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

nav = Player(session=session)

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

sub = Subtitle(session=session)

sub.on()

print(sub.select_next())
{
  'id': 1,
  'jsonrpc': '2.0',
  'result':
        { 
            'currentsubtitle':
                {
                    'index': 1,
                    'language': 'fre',
                    'name': 'French
                }
        }
}
```

| Buttons  |  Description |
|----------|--------------|
| press_on() | ON button |
| press_on() | OFF button |
| select_next() | NEXT button |
| select_previous() | PREVIOUS button |

## Audio track selection

```python
from kodi_remotecontrol import Audio

aud = Audio(session=session)

print(aud.select_next())
{ 
  'id': 1,
  'jsonrpc': '2.0',
  'result':
        {
            'currentaudiostream': 
                {
                    'bitrate': 640000,
                    'channels': 6,
                    'codec': 'ac3',
                    'index': 0,
                    'language': 'fre',
                    'name': 'AC3 5.1(side)'
                }
        }
}
```

| Buttons  |  Description |
|----------|--------------|
| select_next() | NEXT button |
| select_previous() | PREVIOUS button |
