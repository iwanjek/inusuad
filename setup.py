import os
import datetime


def check_directory(cur_dir):
    if not os.path.exists(cur_dir):
        os.makedirs(cur_dir)


def check_months(cur_year):
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    for i in range(len(months)):
        check_directory(cur_year + "\\" + months[i])


def main():
    cur_year = "chronicle" + "\\" + str(datetime.datetime.now().year)
    check_directory(cur_year)
    check_months(cur_year)


main()