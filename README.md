TwilightTime-MP3-Player
=======================

A simple, automagical one button mp3 player for playing music with a sleep timer.

This project leans heavily on theonebuttonaudiobookplayer featured here:
http://blogs.fsfe.org/clemens/2012/10/30/the-one-button-audiobook-player/


Why: We have an alarm clock with nature sounds that are nice to go to sleep by and it has a sleep timer which we enjoy using.
Our cd player in the bedroom has a large anoying blue LED which stays on unless you shut the cd player off.
What we wanted was a simple mp3 player that we could upload files to, press a button and have it play audio for about 30 minutes and then fade out and go to sleep.


Hardware: 

1 Raspberry Pi
1 opaque (ModMyPi?) enclosure
1 button
2 resistors (330 Ohm, 10 Kilo-Ohm) ???
1 8GB SD-Card < link to compatibility list> (I'm using a samsung card)
some wire
Dell AX-210 USB speakers

Software:
Raspian image: 
Maybe use the following in final production:
Raspbian minimal image (http://www.linuxsystems.it/2012/06/raspbian-wheezy-armhf-raspberry-pi-minimal-image)
mpd (music player daemon) http://www.musicpd.org/
mpc
mpd-python 
http://jatreuman.indefero.net/p/python-mpd/ 
http://mpd.wikia.com/wiki/ClientLib:python-mpd2
pyudev (for USB access)
a simple python script

Requirement / Feature List:

always on: When you power on the raspberry, it will boot up and start the python script and wait for a buttom press

one button usage: The button starts the playlist, plays for 30 minutes and then stops. Holding down the button for (3) seconds causes unit to pause or stop playing.

Random play: randomly plays mp3s from folder when button is played

Fade out: at the end of the 30 minutes, the audio stream will fade out. (so you don't wake up when it stops.)

FTP upload: As long as the player isn't playing FTP can be used to upload songs to a music library folder

multi format: Since it uses mpd, the player supports Ogg Vorbis, FLAC, OggFLAC, MP2, MP3, MP4/AAC, MOD, Musepack and wave
