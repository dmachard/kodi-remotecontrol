# Python client for Kodi Server

This is a Python remote control for Kodi Server throught the REST API.

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

| Buttons  |  Description |
|----------|--------------|
| press_up() | UP button |
|------------|--------------------|
| press_down() | DOWN button |
|--------------|----------------------|
| press_left() | LEFT button |
|--------------|----------------------|
| press_right() | RIGHT button |
|--------------|----------------------|
| press_back() | BACK button |
|--------------|----------------------|
| press_enter() | ENTER button |
|--------------|----------------------|
| press_contextmenu() | CONTEXT MENU button |
|--------------|----------------------|

```python
from kodi_remotecontrol import Navigation

nav = Navigation(session=session)

nav.press_up()
```

## Player interaction

| Buttons  |  Description |
|----------|--------------|
| press_play() | PLAY button |
|------------|--------------------|
| press_stop() | STOP button |
|------------|--------------------|
| press_pause() | PAUSE button |
|------------|--------------------|
| press_shuffle() | SHUFFLE button |
|------------|--------------------|
| press_previous() | PREVIOUS button |
|------------|--------------------|
| press_next() | NEXT button |
|------------|--------------------|
| press_info() | INFO button |
|------------|--------------------|

```python
from kodi_remotecontrol import Player

nav = Player(session=session)

nav.press_shuffle()
```

## Subtitle selection

| Buttons  |  Description |
|----------|--------------|
| press_on() | ON button |
|----------|--------------|
| press_on() | OFF button |
|----------|--------------|
| select_next() | NEXT button |
|----------|--------------|
| select_previous() | PREVIOUS button |
|----------|--------------|

```python
from kodi_remotecontrol import Subtitle

sub = Subtitle(session=session)

sub.on()
sub.select_next()
```

## Audio track selection

| Buttons  |  Description |
|----------|--------------|
| select_next() | NEXT button |
|----------|--------------|
| select_previous() | PREVIOUS button |
|----------|--------------|

```python
from kodi_remotecontrol import Audio

aud = Audio(session=session)

aud.select_next()
```