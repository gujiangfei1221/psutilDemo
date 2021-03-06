# -*- coding = utf-8 -*-
import psutil,pymysql,socket,time

def get_cpuinfo():
    num = 0
    times = 5
    for i in range(0,times):
        num = num + psutil.cpu_percent(interval=1, percpu=False)
    num = num/times
    return num

def get_memory():
    times = 5
    totalnum = 0
    availabelnum = 0
    percentnum = 0
    usednum = 0
    for i in range(0,times):
        m_memory = psutil.virtual_memory()
        totalnum = totalnum + m_memory.total
        availabelnum = availabelnum + m_memory.available
        percentnum = percentnum + m_memory.percent
        usednum = usednum + m_memory.used
    totalnum = totalnum/times
    availabelnum = availabelnum/times
    percentnum = percentnum/times
    usednum = usednum/times
    return totalnum,availabelnum,percentnum,usednum

def get_network():
    times = 5
    sentnum = 0
    recvnum = 0
    for i in range(0,times):
        m_network = psutil.net_io_counters(pernic=False)
        time.sleep(1)
        m_network2 = psutil.net_io_counters(pernic=False)
        sentnum = sentnum + (m_network2.bytes_sent - m_network.bytes_sent)
        recvnum = recvnum + (m_network2.bytes_recv - m_network.bytes_recv)
    sentnum = sentnum/times
    recvnum = recvnum/times
    return sentnum,recvnum

def get_diskuseage():
    # m_list = []
    m_disk = psutil.disk_partitions(all=True)
    total = 0
    used = 0
    free = 0
    for i in m_disk:
        path = i.device
        fstype = i.fstype
        if(path != None and fstype != ''):
            path = path.replace('\\','/')
            m_useage = psutil.disk_usage(path)
            total = total + m_useage.total
            used = used + m_useage.used
            free = free + m_useage.free
    return total,used,free

def get_diskio():
    times = 5
    read = 0
    write = 0
    for i in range(0,times):
        m_diskio = psutil.disk_io_counters(perdisk=False)
        time.sleep(1)
        m_diskio2 = psutil.disk_io_counters(perdisk=False)
        read = read + (m_diskio2.read_bytes - m_diskio.read_bytes)
        write = write + (m_diskio2.write_bytes - m_diskio.write_bytes)
    read = read/times
    write = write/times
    return read,write

def get_nameandip():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myname,myaddr

def handle():
    cpu_percent = str(get_cpuinfo())
    memory_total = str(get_memory()[0]/1024/1024)
    memory_available = str(get_memory()[1]/1024/1024)
    memory_usepercent = str(get_memory()[2])
    memory_used = str(get_memory()[3]/1024/1024)
    network_sent = str(get_network()[0]/1024)
    network_recv = str(get_network()[1]/1024)
    diskio_read = str(get_diskio()[0]/1024)
    diskio_write = str(get_diskio()[1]/1024)
    disk_total = str(get_diskuseage()[0]/1024/1024)
    disk_used = str(get_diskuseage()[1]/1024/1024)
    disk_free = str(get_diskuseage()[2]/1024/1024)
    name = str(get_nameandip()[0])
    ip = str(get_nameandip()[1])
    m_time = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='knowledgelibrary', port=3306,charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute('insert into fuwuqi(name,ip,cpu_percent,memory_total,memory_available,memory_percent,memory_used,network_sent,network_recv,disk_read,disk_write,disk_total,disk_used,disk_free,time) values(\''+name+'\',\''+ip+'\',\''+cpu_percent+'\',\''+memory_total+'\',\''+memory_available+'\',\''+memory_usepercent+'\',\''+memory_used+'\',\''+network_sent+'\',\''+network_recv+'\',\''+diskio_read+'\',\''+diskio_write+'\',\''+disk_total+'\',\''+disk_used+'\',\''+disk_free+'\',\''+m_time+'\')')
        conn.commit();
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源

    except  Exception as e:
        print(e.args)


if __name__ == "__main__":
    # print(get_cpuinfo())
    # print(get_memory())
    # print(get_network())
    # print(get_diskuseage())
    # print(get_diskio())
    for i in range(1,20):
        handle()
    # get_nameandip()
    # for i in range(1,100):
    #     m = psutil.disk_io_counters(perdisk=False)
    #     time.sleep(1)
    #     m2 = psutil.disk_io_counters(perdisk=False)
    #     print(m2.read_bytes-m.read_bytes,m2.write_bytes-m.write_bytes)
    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))




