import subprocess

subprocess.call(" figlet FosWink", shell=True)

ans = True



## Functions

def startserver():
    print("Starting Server")


def stopserver():
    print("Stoping Server")


def config():
    print("Config this server!")


def console():
    print("Console Text")


def logs():
    print("Catch the Tail for the logs")


print("FosWink Main Menu")


# Main Loop for MainMenu
while ans:
    ans = raw_input("[FosWink]~> ")

    if ans == "help":

        print("start : Start Gmod server ")
        print("stop : Stop Gmod server ")
        print("config : Change server parameters ")
        print("console : Opens server console ")
        print("logs : Opens Log Manager ")
        print("exit : Exit FosWink ")

    elif ans == "start":

        startserver()

    elif ans == "stop":

        stopserver()

    elif ans == "config":

        config()

    elif ans == "console":

        console()

    elif ans == "logs":

        logs()

    elif ans == "exit":
        break

    else:
        print("Not A Valid Choice, Try again or run help")


