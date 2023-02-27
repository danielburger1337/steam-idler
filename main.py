from steam.client import SteamClient
from csgo.client import CSGOClient
from steam.client.user import SteamUser
from pathlib import Path
from steam.steamid import SteamID
from steam.enums import EType
import os

STEAM_SENTRY_LOCATION = './.steam-sentry'
Path(STEAM_SENTRY_LOCATION).mkdir(parents=True, exist_ok=True)

client = SteamClient()
client.set_credential_location(STEAM_SENTRY_LOCATION)

comanndUserId = SteamID(os.environ.get('STEAM_COMMAND_USER'))
if (comanndUserId.type != EType.Individual):
    raise Exception('No or invalid command user defined')
commandUser = SteamUser(comanndUserId.as_64, client)

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
def handle_login():
    client.change_status(persona_state=client.persona_state.Snooze)
    print(f'Successfully logged in as "{client.user.name}"')

@client.on(client.EVENT_CHAT_MESSAGE)
def auto_respond(user: SteamUser, message: str):
    print(f'{user.name} sent message: "{message}"')

    if commandUser.steam_id.as_64 != user.steam_id.as_64:
        # Generic reply
        user.send_message('Hi, I\'m currency logged in via a CLI script and am unable to respond. Thank you for your message and I will be in touch ASAP.')
        # Send a copy of the message to the command user
        commandUser.send_message(f'{user.name} sent message: {message}')
        return

    messageLower = message.lower()
    if messageLower == '.stop':
        cs.exit()
    elif (messageLower == '.start'):
        cs.launch()
    else:
        commandUser.send_message('Sorry, I dont know this command.')


username = os.environ.get('STEAM_USERNAME')
password = os.environ.get('STEAM_PASSWORD')

client.cli_login(username if username is not None else '',password if password is not None else '')
client.run_forever()
