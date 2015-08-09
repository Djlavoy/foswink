import subprocess
import os


subprocess.call(" figlet FosWink", shell=True)

#Config Vars

SteamDir = "steam"
GmodDir = "gmod"
GmodID = 4020
login = "anonymous"
SteamCMD = "http://media.steampowered.com/client/steamcmd_linux.tar.gz"
SystemOS = "ubuntu"

## Functions

def startserver():
    #TODO, Start screen run command to start server
    print("Starting Server")


def stopserver():
    #TODO, Stop server then end screen
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
    if os.path.exists(SteamDir):
        print("Directory {} Already Exist Skipping".format(SteamDir))
    else:
        print("Directory {} Not Dectected Creating {}".format(SteamDir, SteamDir))
        os.makedirs(SteamDir)
        print("Directory {} Created!".format(SteamDir))

        print("Getting SteamCMD")
        subprocess.call("wget -P {} {}".format(SteamDir, SteamCMD), shell=True)

        print("Extracting SteamCMD")
        subprocess.call("tar -zxvf {}/steamcmd_linux.tar.gz".format(SteamDir), shell=True)

        arch = subprocess.call("uname -m", shell=True)

        if arch == "x86_64":

            print("Getting 32bit Libs\n")

            if SystemOS == "Ubuntu":
                subprocess.call("sudo apt-get -y install lib32stdc++6", shell=True)
            elif SystemOS == "Centos":
                subprocess.call("yum install -y glibc.i686 libstdc++.i686", shell=True)
            elif SystemOS == "Arch":
                subprocess.call("pacman -S lib32-gcc-libs", shell=True);
            else:
                print("You have to set SystemOS to ether Ubuntu, Centos, or Arch\n")
        else:
            print("32Bit System No need to install Libs\n")

        print("Running SteamCMD\n")
        subprocess.call("bash {}/steamcmd.sh +login {} +force_install_dir {} +app_update {} +quit".format(login, GmodDir, GmodID), shell=True)

        print("Completed: Gmod is Located in {}\n".format)




def update():
    print("Updating Gmod")
    subprocess.call("bash {}/steamcmd.sh +login {} +force_install_dir {} +app_update {} +quit".format(login, GmodDir, GmodID), shell=True)

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


