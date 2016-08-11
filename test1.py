#-*- coding = utf-8 -*-
import psutil

#--------------cpu--------------------------
# print(psutil.cpu_times(percpu = True))

# print(psutil.cpu_percent(interval=1, percpu=True))

# print(psutil.cpu_times_percent(interval=1, percpu=True))

# print(psutil.cpu_count(logical=True))

# print(psutil.cpu_stats())

#---------------memory-----------------------
# print(psutil.virtual_memory())

# print(psutil.swap_memory())

#---------------disk-------------------------
# print(psutil.disk_partitions(all=False))

# print(psutil.disk_usage('/'))

# print(psutil.disk_io_counters(perdisk=True))

#---------------network-----------------------
# print(psutil.net_io_counters(pernic=True))

# print(psutil.net_connections())

# print(psutil.net_if_addrs())

# print(psutil.net_if_stats())

#-------------sysinfo------------
# print(psutil.boot_time())

# print(psutil.users())