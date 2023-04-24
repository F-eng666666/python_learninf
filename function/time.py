import time
from datetime import datetime

time_1=time.strftime("%Y-%m-%d %H:%M:%S")
print(time_1)
time.sleep(5)
time_2=time.strftime("%Y-%m-%d %H:%M:%S")
print(time_2)
time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")
seconds = (time_2_struct - time_1_struct).seconds
print(seconds)