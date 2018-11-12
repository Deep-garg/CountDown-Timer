import datetime
import time

target_time = datetime.datetime.now() + datetime.timedelta(days=15)

def get_remaining_time():
    delta = target_time - datetime.datetime.now()

    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    print('{} days: {} hours: {} minutes: {} seconds'.format(delta.days, hours, minutes, seconds), end = '\r')


while target_time!=datetime.datetime.now:
    get_remaining_time()
    time.sleep(1)
    
