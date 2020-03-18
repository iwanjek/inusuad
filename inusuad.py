import configparser
import time
from datetime import datetime


def intro(intro_file):
    f = open(intro_file, "r")
    print(f.read())
    time.sleep(4)

    now = datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))



###################
# MAIN
###################

def main():

    config = configparser.ConfigParser()
    config.read('setup.cfg')

    intro_file = config.get('paths', 'logo')
    intro(intro_file)


main()
