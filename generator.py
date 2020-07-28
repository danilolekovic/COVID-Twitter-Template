import subprocess
from pathlib import Path
import shutil
import fileinput

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def main():
    print("@danilolekovic/COVID-Twitter-Bot customizer script")
    countryName = input("What is your country's name? ")
    govLeader = input("What is your government official's Twitter? (leave blank for none) @")

    dirpath = Path("COVID-Twitter-Bot")

    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    git("clone", "https://github.com/danilolekovic/COVID-Twitter-Bot.git")

    with fileinput.FileInput("COVID-Twitter-Bot/bot.js", inplace=True, backup=".bak") as file:
        for line in file:
            print(line.replace("Canada", countryName), end="")
    
    if len(govLeader) > 0:
        with fileinput.FileInput("COVID-Twitter-Bot/retweet.js", inplace=True, backup=".bak") as file:
            for line in file:
                print(line.replace("CanadianPM", govLeader), end="")

    print("Done. Check ./COVID-Twitter-Bot/")

main()