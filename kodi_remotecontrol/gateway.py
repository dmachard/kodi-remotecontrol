import asyncio
import json
import websockets
import time
import argparse
import logging

from kodi_remotecontrol import eventclient

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("--destport", type=int,
                    default=9777,
                    help="destination backend udp port default=9777")
parser.add_argument("--desthost", type=str,
                    default="127.0.0.1",
                    help="destination backend host address default=127.0.0.1"), 
parser.add_argument("--bindport", type=int,
                    default=8081,
                    help="bind on port default=8081")
parser.add_argument("--bindhost", type=str,
                    default="0.0.0.0",
                    help="bind on host default=0.0.0.0")
              
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
            logging.debug("trying to press on button: %s" % data["button"])

            try:
                press_function = getattr(eventapi, data["button"])
                press_function()
            except AttributeError as e:
                logging.error("unsupported press button %s" % e)
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