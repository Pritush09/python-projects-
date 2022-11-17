import time
def countdown(time_sec):
    while time_sec>0:
        minute , sec = divmod(time_sec,60)
        time_format = "{:02d}:{:02d}".format(minute,sec)
        print(time_format,'\r')
        time.sleep(1)
        time_sec -= 1
    print("TIME ENDED")
countdown(500)

