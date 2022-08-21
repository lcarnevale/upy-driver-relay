"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

import _thread
from time import sleep
from driver.relay import Relay

def loop(relay):
    while True:
        relay.high()
        sleep(2)
        relay.low()
        sleep(2)

def main():
    pin = 26
    relay = Relay().build_pin(pin)
    args = (relay,)
    _thread.start_new_thread(loop, args)

main()