#!/usr/bin/env python
#  Copyright (C) 2012 Gray Anthony
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import RPi.GPIO as GPIO
import os
import pyudev

from mpd import (MPDClient, CommandError)
from socket import error as SocketError
from time import sleep

# Configure MPD connection settings
HOST = 'localhost'
PORT = '6600'
CON_ID = {'host':HOST, 'port':PORT}

# Configure IO ports
BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

## Some functions
def mpdConnect(client, con_id):
        """
        Simple wrapper to connect MPD.
        """
        try:
                client.connect(**con_id)
        except SocketError:
                return False
        return True

# need to rewrite to point to ftp root or copy from ftp root to mp3 location
def loadMusic():

         os.system("mpc update")			
         os.system("mpc clear")
         os.system("mpc ls | mpc add")

def fadeout():
		#decrease volume by 2 every second, then stop.
		volume = client.volume()  # is this right?
		while volume > 10: # verify this value is low enough
				volume -= 2
				client.setvol(volume)
		client.stop()


def main():
        ## MPD object instance
        client = MPDClient()
        mpdConnect(client, CON_ID)

        print client.status()
        
        timeButtonIsPressed = 0
        playCounter = 0

        while True:
                
                print client.status()
                

				## respond to the button press
                if GPIO.input(BUTTON) == True:
                        if timeButtonIsPressed == 1:
                                # button has been pressed 1 sec, stop or play now
                                if client.status()["state"] == "stop":
                                		loadMusic()
                                        client.play()
                                else:
                                        client.stop()

                        timeButtonIsPressed = timeButtonIsPressed + 0.1
                        
                else:
                        timeButtonIsPressed = 0
                        if client.status()["state"] == "play":
                        		playCounter += 0.1

                sleep(0.1)
            	if playCounter > 1800
            			fadeOut()
                

# Script starts here
if __name__ == "__main__":
    main()
