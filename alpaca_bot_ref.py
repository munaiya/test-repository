# Functions, variables used in alpaca_bot.py is kept here
# Designed and developed by Field Marshal Prabir Kumar
import datetime as dt
import time as t


def get_curr_date_time():
    # Will return time as per ET
    current_time = dt.datetime.now()
    return current_time


def get_unix_time(date_time):
    # Will accept date_time as input parameter and return unix_time
    unix_time = t.mktime(date_time.timetuple())
    return int(unix_time)



