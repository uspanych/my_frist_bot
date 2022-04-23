import datetime
import time


# TODO: посмотреть https://apscheduler.readthedocs.io/en/3.x/
while True:
    timeobj = str(datetime.time(14, 0, 0))[:2]
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())[:2]
    if timeobj == current_time:
        print('+++')
