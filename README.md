# CS:GO Hour Booster

The script will automatically ask you for your credentials and optional 2FA code (provided by [ValvePython/steam](https://github.com/ValvePython/steam)).

```sh
pip install -r requirements.txt

python3 main.py
```

---

## Persistant Login

1. Create a file called `credentials.txt`
2. First line must contain your username, second line your password

```txt
username
password
```

3. Execute the script with the file path as argument

```sh
python3 main.py credentials.txt
```

After you have successfully logged in for the first time, the sentry created by steam is automatically saved to the `.steam-sentry` directory and future executions of the script will auto login.

If this was setup correctly, you can than run the script as a background process with the following command:

```sh
nohup python3 main.py credentials.txt

# To kill the process
pkill -f main.py
```

`nohup` is a linux utility that prevents a process from shutting down when the terminal session was closed.

---

## Automatic chat reply

Because this script is intended to be run headless (i.e. on a server), the script will automatically reply to all received chat messages with a simple message that lets your friends know that you are currently not available.
