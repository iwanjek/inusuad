import configparser
from datetime import datetime
import dateutil.parser
import random
import json


def getDateTimeFromISO8601String(s):
    d = dateutil.parser.parse(s)
    return d

class Goal:
    def __init__(self, goal, smart, inception_date):
        self.goal = goal
        self.smart = smart
        self.inception_date = inception_date


def save(entry):
    #save dict to text in json
    type = entry['__class__']
    if type == 'JournalPage':
        date = getDateTimeFromISO8601String(entry['date'])
        year = date.strftime("%Y")
        month = date.strftime("%b")
        month = month.upper()
        day = date.strftime("%d")

        file_name = day + month + year + ".json"
        path = "chronicle" + "\\" + year + "\\" + month + "\\" + file_name
        with open(path, 'w') as outfile:
            json.dump(entry, outfile)
            print("Saved: " + file_name)


def convert_to_dict(obj):
    # Take custom object and turn it into a dict
    obj_dict = dict(__class__=obj.__class__.__name__, __module__=obj.__module__)
    obj_dict.update(obj.__dict__)

    return obj_dict


def get_self_reflect():
    config = configparser.ConfigParser()
    config.read('setup.cfg')

    reflect_file = config.get('paths', 'reflect')
    f = open(reflect_file, "r")
    lines = f.readlines()

    reflect_question = random.choice(lines)

    return reflect_question


class JournalPage:
    def __init__(self, uniq_yesterday, feeling, lucky, reflect_question, reflect, entry):
        self.uniq_yesterday = uniq_yesterday
        self.feeling = feeling
        self.lucky = lucky
        self.reflect_question = reflect_question
        self.reflect = reflect
        self.entry = entry
        self.date = datetime.now().isoformat()
