from datetime import datetime  as dt
from time import strftime
import user_interface as ui

def logger():
    data = ui.choice()[2]
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{} {} \n'.format(time,data))
