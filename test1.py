#-*- coding = utf-8 -*-
import psutil

print(psutil.cpu_times())

for x in range(3):
    print(psutil.cpu_percent(interval=1))