import os
import datetime


def check_directory(cur_dir):
    if not os.path.exists(cur_dir):
        os.makedirs(cur_dir)


def check_months(cur_year, quarter, quarter_start, quarter_end):
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    for i in range(quarter_start, quarter_end):
        check_directory(cur_year + "\\" + quarter + "\\" + months[i])


def check_quarters(cur_year):
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    quarter_start = 0
    quarter_end = 3
    for quarter in quarters:
        check_directory(cur_year + "\\" + quarter)
        check_months(cur_year, quarter, quarter_start, quarter_end)
        quarter_start = quarter_end
        quarter_end = quarter_end + 3


def main():
    cur_year = str(datetime.datetime.now().year)
    check_directory(cur_year)
    check_quarters(cur_year)


main()
