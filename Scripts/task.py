import datetime
import time
import schedule
import os

def job():
    os.system(f'python EmptyStandbyList.exe')
    

schedule.every(5).seconds.do(job)

while(True):
    schedule.run_pending()
    time.sleep(1)
    