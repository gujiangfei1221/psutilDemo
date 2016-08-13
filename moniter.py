# -*- coding = utf-8 -*-
import psutil,pymysql,socket

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
        sentnum = sentnum + m_network.bytes_sent
        recvnum = recvnum + m_network.bytes_recv
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
    m_diskio = psutil.disk_io_counters(perdisk=False)
    for i in range(0,times):
        read = read + m_diskio.read_bytes
        write = write + m_diskio.write_bytes
    read = read/times
    write = write/times
    return read,write

def get_ip():
    pass

def handle():
    cpu_percent = get_cpuinfo()
    memory_total = get_memory()[0]/1024/1024
    memory_available = get_memory()[1]/1024/1024
    memory_usepercent = get_memory()[2]
    memory_used = get_memory()[3]/1024/1024
    network_sent = get_network()[0]/1024/1024
    network_recv = get_network()[1]/1024/1024
    diskio_read = get_diskio()[0]
    diskio_write = get_diskio()[1]
    disk_total = get_diskuseage()[0]
    disk_used = get_diskuseage()[1]
    disk_free = get_diskuseage()[2]

    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='knowledgelibrary', port=8889,charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute('insert into fuwuqi() values()')
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
    # handle()
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    print(myname,myaddr)




