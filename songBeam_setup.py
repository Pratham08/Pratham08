import os
from datetime import datetime

playlist = 'play1'

current_time = str(datetime.now())

set_hour = 10
set_min = 5

def call_songbeam():
    os.system(f'python songBeam.py {playlist}')
    
while True:
    hour = int(current_time[11:13])
    minutes = int(current_time[14:16])
    if hour==set_hour and minutes==set_min:
        call_songbeam()
        exit()
        
