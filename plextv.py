# Usage: plextv.py [device] [tv show]
# Example: plextv.py 'roku tv' 'the office'
# Notes: This selectes a random episode and plays with shuffle enabled
# Dependencies: pip3 install plexapi
# How to get auth token: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

from time import sleep
from plexapi.myplex import PlexServer
from random import randrange
import sys

device_name = sys.argv[1]
call_show = sys.argv[2]

baseurl  = 'http://plex.home.com:32400'

token = ''

#for client in plex.clients():
#    print(client.title)

tries = 5
for i in range(tries):
    try:
        plex = PlexServer(baseurl,token)
        show = plex.library.section('TV Shows').get(call_show).episodes()
        g_range = randrange(len(show))

        client = plex.client(device_name)
        client.playMedia(show[g_range])
        client.setShuffle(1)
    except Exception as e:
        if i < tries - 1: # i is zero indexed
            print("oops we had a failure....yawn")
            sleep(5)
            continue
        else:
            raise
    break
#client.playMedia(show[g_range])


