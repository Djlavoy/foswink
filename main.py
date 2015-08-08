import subprocess

subprocess.call(" figlet FosWink", shell=True)

## Functions

def startserver():
    print("Starting Server")


def stopserver():
    print("Stoping Server")


def bans():
    print("Ban Manager")


def config():
    print("Config this server!")


def console():
    print("Console Text")


def logs():
    print("Catch the Tail for the logs")


def installer():
    print("Gmod Installer")


def update():
    print("Updating Gmod")


def mountgames():
    print("Mounting Games")


# Main Loop for MainMenu

print("FosWink Main Menu")

ans = True

while ans:
    ans = raw_input("[FosWink]~> ")

    if ans == "help":

        print("start : Start Gmod server ")
        print("stop : Stop Gmod server ")
        print("bans : Opens Ban Manager")
        print("config : Change server parameters ")
        print("console : Opens server console ")
        print("logs : Opens Log Manager ")
        print("installer : Install Gmod")
        print("mount : Mount Games to Gmod")
        print("exit : Exit FosWink ")

    elif ans == "start":

        startserver()

    elif ans == "stop":

        stopserver()

    elif ans == "ban":

        bans()

    elif ans == "config":

        config()

    elif ans == "console":

        console()

    elif ans == "logs":

        logs()

    elif ans == "installer":

        installer()

    elif ans == "update":

        update()

    elif ans == "mount":

        mountgames()

    elif ans == "exit":
        break

    else:
        print("Not A Valid Choice, Try again or run help")


