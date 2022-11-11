import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import binascii
master = mt.TcpMaster('192.168.1.10', 502)
master.set_timeout(2)
bianhao = {'1-Num': 0, '1-Kx': 5, '1-Gg': 10, '1-Gx': 15}


def yaochuang(N, L=500):
    data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=L+N,
                          quantity_of_x=5)
    xinhao = ''
    for i in range(0, 5):
        a = hex(data[i])
        b = a[2:]
        b2 = ''
        if b != '0' and b[2:] != '':
            b = binascii.a2b_hex(b)
            b2 = str(b, encoding="utf-8")
            b2 = b2[1]+b2[0]
        elif b !='0' and b[2:] == '':
            b = binascii.a2b_hex(b)
            b2 = str(b, encoding="utf-8")
        xinhao +=b2
    print(xinhao)
    return xinhao
yaochuang(0)
yaochuang(5)
yaochuang(10)
yaochuang(15)
yaochuang(20)
yaochuang(25)
yaochuang(30)
yaochuang(35)
yaochuang(40)
yaochuang(45)
yaochuang(50)
yaochuang(55)
yaochuang(60)
yaochuang(65)
yaochuang(70)
yaochuang(75)
yaochuang(80)
yaochuang(85)
yaochuang(90)
yaochuang(95)
yaochuang(0,600)
yaochuang(5,600)
yaochuang(10,600)
yaochuang(15,600)
yaochuang(20,600)
yaochuang(25,600)
yaochuang(30,600)
yaochuang(35,600)
yaochuang(40,600)
yaochuang(45,600)
yaochuang(50,600)
yaochuang(55,600)
yaochuang(60,600)
yaochuang(65,600)
yaochuang(70,600)
yaochuang(75,600)
yaochuang(80,600)
yaochuang(85,600)
yaochuang(90,600)
yaochuang(95,600)
yaochuang(0,700)
yaochuang(5,700)
yaochuang(10,700)
yaochuang(15,700)
yaochuang(20,700)
yaochuang(25,700)
yaochuang(30,700)
yaochuang(35,700)
yaochuang(40,700)
yaochuang(45,700)
yaochuang(50,700)
yaochuang(55,700)
yaochuang(60,700)
yaochuang(65,700)
yaochuang(70,700)
yaochuang(75,700)
yaochuang(80,700)
yaochuang(85,700)
yaochuang(90,700)
yaochuang(95,700)
yaochuang(0,800)
yaochuang(5,800)
yaochuang(10,800)
yaochuang(15,800)
yaochuang(20,800)
yaochuang(25,800)
yaochuang(30,800)
yaochuang(35,800)
yaochuang(40,800)
yaochuang(45,800)
yaochuang(50,800)
yaochuang(55,800)
yaochuang(60,800)
yaochuang(65,800)
yaochuang(70,800)
yaochuang(75,800)
yaochuang(80,800)
yaochuang(85,800)
yaochuang(90,800)
yaochuang(95,800)

# PLC侧从数据寄存器200-299表示机型1-100对应设备当天的切机型次数
data_qiejicishu = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=200,
                      quantity_of_x=20)
print(data_qiejicishu)
# PLC侧从数据寄存器100-199表示机型1-100对应设备的开机状态
data_kaiji = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=100,
                            quantity_of_x=20)
list_data = list(data_kaiji)
kaijishu = list_data.count(100)
kaijilv = format((float(kaijishu) / 37) * 100, '.2f')
print(kaijilv)
# PLC侧从数据寄存器300-399表示机型1-100对应设备当前机型的产量
data_dq_cl = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=300,
                            quantity_of_x=20)
print(data_dq_cl)
# PLC侧从数据寄存器400-499表示机型1-100对应设备当天总产量
data_dt_cl = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=400,
                            quantity_of_x=20)
print(data_dq_cl)
print(str(data_dq_cl[0]))
"""
b1 = b'Hello'
s1 = 'Hello'
print(type(b1))
print(type(s1))
# bytes类型转换为str类型
# 方法1 str()函数
s2 = str(b1, encoding="utf-8")
print(s2)
print(type(s2))
# 方法2 bytes.decode()函数
s3 = bytes.decode(b1)
print(s3)
print(type(s3))
"""