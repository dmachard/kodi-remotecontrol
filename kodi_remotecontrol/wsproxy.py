import asyncio
import json
import websockets
import time
import argparse
import logging

from kodi_remotecontrol import eventclient

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("--destport", type=int, default=9777, help="destination kodi port default=9777")
parser.add_argument("--desthost", type=str, default="127.0.0.1", help="destination kodi host default=127.0.0.1"), 
parser.add_argument("--bindport", type=int, default=8081, help="bind on port default=8081")
parser.add_argument("--bindhost", type=str, default="0.0.0.0", help="bind on host default=0.0.0.0")

# parse provided arguments and logging
args = parser.parse_args()
logging.debug( args )

eventapi = None

async def handle_message(websocket, path):
    """handle websocket messages"""
    global eventapi
    try:
        async for message in websocket:
            # decode message, json expected
            data = json.loads(message)

            if "button" not in data:
                raise Exception("bad received message, button is missing")
            logging.debug("button pressed: %s" % data["button"])

            # player
            if data["button"] == "press_play":
                eventapi.send_action(msg="Action(Play)")
            elif data["button"] == "press_pause":
                eventapi.send_action(msg="Action(Pause)")
            elif data["button"] == "press_stop":
                eventapi.send_action(msg="Action(Stop)")
            elif data["button"] == "press_osd":
                eventapi.send_action(msg="Action(OSD)")
            elif data["button"] == "press_playlist":
                eventapi.send_action(msg="Action(Playlist)")
            elif data["button"] == "press_next":
                eventapi.send_action(msg="Action(SkipNext)")
            elif data["button"] == "press_previous":
                eventapi.send_action(msg="Action(SkipPrevious)")
            # navigation
            elif data["button"] == "press_left":
                eventapi.send_action(msg="Action(Left)")
            elif data["button"] == "press_right":
                eventapi.send_action(msg="Action(Right)")
            elif data["button"] == "press_up":
                eventapi.send_action(msg="Action(Up)")
            elif data["button"] == "press_down":
                eventapi.send_action(msg="Action(Down)")
            elif data["button"] == "press_enter":
                eventapi.send_action(msg="Action(Select)")
            elif data["button"] == "press_back":
                eventapi.send_action(msg="Action(Back)")
            elif data["button"] == "press_ctxmenu":
                eventapi.send_action(msg="Action(ContextMenu)")
            # system
            elif data["button"] == "press_reset":
                eventapi.refresh_connection()
            elif data["button"] == "press_logoff":
                eventapi.send_action(msg="System.LogOff")
            # subtitle
            elif data["button"] == "press_subtitle":
                eventapi.send_action(msg="Action(NextSubtitle)")
            # language
            elif data["button"] == "press_language":
                eventapi.send_action(msg="Action(AudioNextLanguage)")
            else:
                raise Exception("unsupported button: %s" % data["button"])    

    except Exception as e:
        logging.error("%s" % e)

async def ping_eventserver():
    """send ping to kodi on eventserver api"""
    global eventapi
    while True:
        # send a ping to the eventserver every 50 seconds
        eventapi.send_ping()
        logging.debug('ping to eventserver')
        await asyncio.sleep(50)

async def wakeup_loop():
    """wakeup to accept keyboard interrupt"""
    while True:
        await asyncio.sleep(1)

def start_remotecontrol():
    """start remote control"""
    global eventapi

    logging.info("Start websocket gateway...")

    # prepare the event client with destination ip/port provided
    eventapi = eventclient.EventClient(api_host=args.desthost, 
                                       api_udp_port=args.destport)

    # prepare the websocket server
    start_server = websockets.serve(handle_message, args.bindhost, args.bindport)

    # get the main event loop
    eventloop = asyncio.get_event_loop()
    # run server
    eventloop.run_until_complete(start_server)
    # hack to support KeyboardInterrupt
    eventloop.create_task(wakeup_loop())
    # schedule the execution of the ping request
    eventloop.create_task(ping_eventserver())

    # run event loop
    try:
        eventloop.run_forever()
    except KeyboardInterrupt:
        pass