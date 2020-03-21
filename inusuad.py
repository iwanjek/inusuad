import configparser

import commonplace
from datetime import datetime
from os import system, name, path, makedirs
from time import sleep


def screen_clear():
    # windows os
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def save_del_redo(obj):
    temp = commonplace.convert_to_dict(obj)
    print(temp)

    answer = input("Enter \"save\" \"del\" or \"redo\" \n")
    answer = answer.lower()
    continue_entry = False
    if answer == "save":
        # here you would begin saving the file into a json file
        temp = commonplace.convert_to_dict(obj)
    elif answer == "del":
        answer = input("Type \"yes\" to confirm delete. \n")
        answer = answer.lower()
        if answer == "yes":
            return continue_entry
        else:
            print("Repeating  request... \n")
            save_del_redo(obj)
    elif answer == "redo":
        continue_entry = True
    else:
        print("Did not understand input. Repeating  request...")
        save_del_redo(obj)

    return continue_entry


def setup():
    if not path.exists('chronicle'):
        makedirs('chronicle')


def intro(intro_file):
    f = open(intro_file, "r")
    print(f.read())

    sleep(4)
    screen_clear()

    now = datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def journal():
    continue_entry = True
    while continue_entry:
        uniq_yesterday = input("What unique experience happened yesterday?\n")
        feeling = input("How are you feeling?\n")
        lucky = input("What makes you lucky?\n")
        reflect_question = commonplace.get_self_reflect()
        reflect = input(reflect_question)
        entry = input("What is today's journal entry?\n")
        today = commonplace.JournalPage(uniq_yesterday, feeling, lucky, reflect_question, reflect, entry)
        continue_entry = save_del_redo(today)


###################
# MAIN
###################

def main():
    config = configparser.ConfigParser()
    config.read('setup.cfg')

    intro_file = config.get('paths', 'logo')
    intro(intro_file)

    journal()
    print("on to next")


main()
