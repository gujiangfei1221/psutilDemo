# -*- coding = utf-8 -*-
import psutil,pymysql

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
    m_list = []
    m_disk = psutil.disk_partitions(all=False)
    for i in m_disk:
        path = i.device
        fstype = i.fstype
        if(path != None and fstype != ''):
            path = path.replace('\\','/')
            m_list.append(psutil.disk_usage(path))
    return m_list

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

def handle():

    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='codeigniter', port=8889,charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute('')
        conn.commit();
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源

    except  Exception as e:
        print(e.args)


if __name__ == "__main__":
    print(get_cpuinfo())
    print(get_memory())
    print(get_network())
    print(get_diskuseage())
    print(get_diskio())




