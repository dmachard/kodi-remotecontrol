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

This remote control acts as a websocket Gateway of the UDP **Event Server** API for more reactivity.
A frontend is available [here](vuejs-client/README.md).

## Table of contents
* [Installation](#installation)
* [Start remote control](#start-remote-control)
* [Available buttons](#available-buttons)
* [Websocket client](#websocket-client)
* [Systemd service](#systemd-service)

## Installation

```python
pip install kodi_remotecontrol
```

## Start remote control

As prerequisite, go to `System/Settings/Network/Services` and activate the two following options
 - `Allow programs on other systems to control Kodi`
 - `Allow control of Kodi via HTTP`
 
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

```json
{"button": "press_up"} // press on up button
{"button": "press_down"} // press on down button
{"button": "press_left"} // press on left button
{"button": "press_right"} // press on right button
{"button": "press_back"} // press on back button
{"button": "press_enter"} // press on enter button
{"button": "press_ctxmenu"} // display contextual menu
{"button": "press_playlist"} // display playlist
{"button": "press_logoff"} // press on logoff button
```

### Player interaction

```json
{"button": "press_play"} // press on play button
{"button": "press_stop"} // press on stop button
{"button": "press_pause"} // press on pause button
{"button": "press_previous"} // press on previous button
{"button": "press_next"} // press on next button
{"button": "press_osd"} // display OSD
```

### Subtitle selection

```json
{"button": "press_subtitle"} // toggle subtitle
```

### Audio track selection

```json
{"button": "press_language"} // toggle language
```

## Websocket client

### Basic demo

```html
<html>
  <head>
      <title>RemoteControl demo</title>
      <style type="text/css">
          .buttons {
              font-size: 1em;
              display: flex;
              justify-content: center;
          }
          .button {
              padding: 2rem;
              border: medium solid;
              min-height: 1em;
              min-width: 1em;
              cursor: pointer;
              user-select: none;
          }
      </style>
  </head>
  <body>
    <div class="buttons">
      <div class="play button">Play</div>
      <div class="pause button">Pause</div>
    </div>
    <script>
      var websocket = new WebSocket("ws://localhost:8081/");

      var play = document.querySelector('.play')
      var pause = document.querySelector('.pause')

      play.onclick = function (event) {
        websocket.send(JSON.stringify({button: 'press_play'}));
      }
      pause.onclick = function (event) {
        websocket.send(JSON.stringify({button: 'press_pause'}));
      }
    </script>
  </body>
</html>
````

## Systemd service

Example of system service file for Centos7

```bash
vim /etc/systemd/system/kodi_remotecontrol.service

[Unit]
Description=Kodi remote control Service
After=network.target

[Service]
ExecStart=/usr/local/bin/kodi_remotecontrol --desthost=10.0.0.200
Restart=on-abort
Type=simple
User=root

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload
systemctl start kodi_remotecontrol
systemctl status kodi_remotecontrol
systemctl enable kodi_remotecontrol
```
