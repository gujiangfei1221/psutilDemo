#-*- coding = utf-8 -*-
import psutil

#--------------cpu--------------------------
# print('cpu_times:',psutil.cpu_times(percpu = True))

# for i in range(1,10):
#     print('cpu_percent:',psutil.cpu_percent(interval=1, percpu=False))

# print('cpu_times_percent:',psutil.cpu_times_percent(interval=1, percpu=True))

# print('cpu_count:',psutil.cpu_count(logical=True))

# print('cpu_stats:',psutil.cpu_stats())

#---------------memory-----------------------
# print('virtual_memory:',psutil.virtual_memory())

# print('swap_memory:',psutil.swap_memory())

#---------------disk-------------------------
# print('disk_partitions:',psutil.disk_partitions(all=False))
#
# print('disk_useage:',psutil.disk_usage('D:/'))

# print('disk_io_counters:',psutil.disk_io_counters(perdisk=True))

#---------------network-----------------------
# print('net_io_counters:',psutil.net_io_counters(pernic=True))
#
# print('net_connections:',psutil.net_connections())
#
# print('net_if_addrs:',psutil.net_if_addrs())
#
print('net_if_stats:',psutil.net_if_stats())
#
# #-------------sysinfo------------
# print('boot_time:',psutil.boot_time())
#
# print('users:',psutil.users())