import configparser
import commonplace
from datetime import datetime
from os import system, name
from time import sleep


def screen_clear():
    #windows os
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def intro(intro_file):
    f = open(intro_file, "r")
    print(f.read())

    sleep(4)
    screen_clear()

    now = datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def journal():
    uniq_yesterday = input("What unique experience happened yesterday?")
    feeling = input("How are you feeling?")
    lucky = input("What makes you lucky?")
    reflect_question = commonplace.get_self_reflect()
    reflect = input(reflect_question)
    entry = input("What is today's journal entry?")

    today = commonplace.JournalPage(uniq_yesterday, feeling, lucky, reflect_question, reflect, entry)






###################
# MAIN
###################

def main():
    config = configparser.ConfigParser()
    config.read('setup.cfg')

    intro_file = config.get('paths', 'logo')
    intro(intro_file)

    journal()


main()
