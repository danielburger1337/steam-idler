import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

from steam.client import SteamClient
from csgo.client import CSGOClient
from steam.client.user import SteamUser
from pathlib import Path
import sys

STEAM_SENTRY_LOCATION = './.steam-sentry'
Path(STEAM_SENTRY_LOCATION).mkdir(parents=True, exist_ok=True)

client = SteamClient()
client.set_credential_location(STEAM_SENTRY_LOCATION)

cs = CSGOClient(client)

@client.on(client.EVENT_CHANNEL_SECURED)
def send_login():
    if client.relogin_available:
        client.relogin()

@client.on(client.EVENT_DISCONNECTED)
def handle_disconnect():
    if (client.relogin_available):
        client.reconnect(30)

@client.on(client.EVENT_LOGGED_ON)
def start_csgo():
    print('Successfully logged in. Launching CSGO...')
    cs.launch()

@client.on(client.EVENT_CHAT_MESSAGE)
def auto_respond(user: SteamUser, message: str):
    print(f'{user.name} sent message: {message}')

    user.send_message('Hi, I\'m currency logged in via a CLI script and am unable to respond. Thank you for your message and I will be in touch ASAP.')


credentials = []

try:
    credPath = Path(sys.argv[1])

    if Path.exists(credPath):
        with open(credPath.absolute()) as my_file:
            for line in my_file:
                credentials.append(line)

    print(f'Using credentials stored in {credPath.absolute()}')
except IndexError:
    pass

if len(credentials) == 2:
    client.cli_login(credentials[0].strip(), credentials[1].strip())
else:
    client.cli_login()

client.run_forever()
