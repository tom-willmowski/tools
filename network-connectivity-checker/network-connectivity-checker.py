from argparse import ArgumentParser
import time
from pygame import mixer
from urllib import urlopen

parser = ArgumentParser(prog="NetworkConnectivityCheck")
parser.add_argument("--ok_sound_path", help="sound path", default="./ok.mp3")
parser.add_argument("--error_sound_path", help="sound path", default="./error.mp3")
parser.add_argument("--interval", help="check interval", type=float, default=5.0)

args = vars(parser.parse_args())

def check_connectivity():
    try:
        urlopen("http://google.com")
        return True
    except IOError:
        return False

mixer.init()

while True:
	is_connected = check_connectivity()
	if is_connected:
		mixer.music.load(args['ok_sound_path'])
		mixer.music.play()
	else:
		mixer.music.load(args['error_sound_path'])
		mixer.music.play()
	time.sleep(args['interval'])