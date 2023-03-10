# Steam Idler

The script will automatically ask you for your credentials and optional 2FA code (provided by [ValvePython/steam](https://github.com/ValvePython/steam)).

```sh
pip install -r requirements.txt

python3 main.py
```

---

## How it works

This script works by having a commander (STEAM_COMMAND_USER) sending chat messages to the currently signed in user
with commands that the bot will follow. Valid commands are:

-   **.start APP_ID** <br> This command starts the specified app id
-   **.stop APP_ID** <br> This command stops the specified app id

```sh
export STEAM_COMMAND_USER="your_steam_id"
```

## Login

To automatically login, you have to define your username and password as environment variables.
The script will automatically use these credentials and will only ask you for your 2FA token (if needed).

```sh
export STEAM_USERNAME="your_username"
export STEAM_PASSWORD="your_password"
```

After you have successfully logged in for the first time, the 2FA-sentry created by steam is automatically saved to the `.steam-sentry` directory and future executions of the script will use it. Please note that steam guard users are always prompted for their 2FA code.

## Docker Usage

Running this script in docker allows us to basically create a background service (so that you can close the terminal without the script execution stopping).

```sh
# Start the script with an interactive shell
docker-compose run --rm --build idler

# To kill the process when you want to
docker-compose kill
```

## Automatic chat reply

Because this script is intended to be run headless (i.e. on a server), the script will automatically reply to all received chat messages with a simple message that lets your friends know that you are currently not available.

A copy of that message is also send to the command user.
