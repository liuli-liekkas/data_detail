import os.path
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 经典两点计算公式
def geo_distance(lng_test, lat_test, lng_ref, lat_ref):
    lng_test = round(lng_test // 100 + lng_test % 100 / 60, 6)
    lat_test = round(lat_test // 100 + lat_test % 100 / 60, 6)
    lng_ref = round(lng_ref // 100 + lng_ref % 100 / 60, 6)
    lat_ref = round(lat_ref // 100 + lat_ref % 100 / 60, 6)
    # 角度转弧度
    lng1, lat1, lng2, lat2 = map(math.radians, [lng_test, lat_test, lng_ref, lat_ref])
    d_lng = lng2 - lng1
    d_lat = lat2 - lat1
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lng / 2) ** 2
    dis = 2 * math.asin(math.sqrt(a)) * 6371 * 1000
    return dis

# 三点计算公式
# def geodistance(lng_test, lat_test, h_test, lng_default, lat_default, h_default):
#     lng_test, lat_test, lng_default, lat_default = map(math.radians, [lng_test, lat_test, lng_default, lat_default])
#     delta_x = h_test * math.cos(lat_test) * math.cos(lng_test) - h_test * math.cos(lat_default) * math.cos(lng_default)
#     delta_y = h_test * math.cos(lat_test) * math.sin(lng_test) - h_test * math.cos(lat_default) * math.sin(lng_default)
#     delta_z = h_test - h_default
#     dis = math.sqrt(delta_x + delta_y + delta_z)
#     return dis


# 数据格式化
filename_ref = 'gnss/test20210830/mtk_combine_dynamic_precision_opensky_ref-f.txt'
filename_test = 'gnss/test20210830/mtk_combine_dynamic_precision_opensky-f.txt'
data_ref_gprmc = {}
data_ref_gpgga = {}
data_test_gnrmc = {}
data_test_gngga = {}
data_detail_final = []
data_speed_final = []
data_high_final = []
data_ref_total_distance = []
data_test_total_distance = []
ref_total_distance = 0
test_total_distance = 0

# 录入参考数据
with open(filename_ref, 'r') as file_ref:
    data_ref = file_ref.readlines()
    num = len(data_ref)
# REF_GPRMC
for line in range(num):
    data_ref_split = data_ref[line].split(',')
    if data_ref_split[0] == '$GLRMC':
        if len(data_ref_split) > 8:
            if data_ref_split[3]:
                data_ref_gprmc[data_ref_split[1]] = [data_ref_split[5],  # 经度
                                                     data_ref_split[3],  # 纬度
                                                     data_ref_split[7]]  # 速度
# REF_GPGGA
for line in range(num):
    data_ref_split = data_ref[line].split(',')
    if data_ref_split[0] == '$GPGGA':
        if len(data_ref_split) > 11:
            if data_ref_split[4]:
                data_ref_gpgga[data_ref_split[1]] = [data_ref_split[4],  # 经度
                                                     data_ref_split[2],  # 纬度
                                                     data_ref_split[9],  # 海平面高度
                                                     data_ref_split[10]]  # 地平面高度

# 录入测试数据_动态点
with open(filename_test, 'r', encoding='utf-8') as file_test:
    data_test = file_test.readlines()
    num = len(data_test)
# TEST_GPRMC
for line in range(num):
    data_test_split = data_test[line].split(',')
    if data_test_split[0] == '$GNRMC':
        if data_test_split[3]:
            data_test_gnrmc[data_test_split[1].split('.')[0]] = [data_test_split[5],  # 经度
                                                                 data_test_split[3],  # 纬度
                                                                 data_test_split[7]]  # 速度
# TEST_GNGGA
for line in range(num):
    data_test_split = data_test[line].split(',')
    if data_test_split[0] == '$GNGGA':
        if data_test_split[3]:
            data_test_gngga[data_test_split[1].split('.')[0]] = [data_test_split[4],  # 经度
                                                                 data_test_split[2],  # 纬度
                                                                 data_test_split[9],  # 海平面高度
                                                                 data_test_split[10]]  # 地平面高度
# 开始比对测试GGA
for key in data_test_gngga:
    if key in data_ref_gpgga.keys():
        high = float(data_test_gngga[key][3]) - float(data_ref_gpgga[key][3])
        data_high_final.append(high)

# 开始比对测试RMC_动态点
for key in data_test_gnrmc:
    if key in data_ref_gprmc.keys():
        distance = geo_distance(float(data_test_gnrmc[key][1]), float(data_test_gnrmc[key][0]),
                                float(data_ref_gprmc[key][1]), float(data_ref_gprmc[key][0]))
        speed = (float(data_test_gnrmc[key][2]) - float(data_ref_gprmc[key][2]))/3.6*1.852

        data_test_total_distance.append([data_test_gnrmc[key][1], data_test_gnrmc[key][0]])
        data_ref_total_distance.append([data_ref_gprmc[key][1], data_ref_gprmc[key][0]])
        data_detail_final.append(distance)
        data_speed_final.append(speed)

# 待测件行驶的里程数
for i in range(0, len(data_test_total_distance)-2):
    test_total_distance += geo_distance(float(data_test_total_distance[i+1][0]),
                                        float(data_test_total_distance[i+1][1]),
                                        float(data_test_total_distance[i][0]),
                                        float(data_test_total_distance[i][1]))
    i += 1

# 基准信号行驶的里程数
for i in range(0, len(data_ref_total_distance)-2):
    ref_total_distance += geo_distance(float(data_ref_total_distance[i+1][0]), float(data_ref_total_distance[i+1][1]),
                                       float(data_ref_total_distance[i][0]), float(data_ref_total_distance[i][1]))
    i += 1

print('距离单位：m，速度单位：m/s')
print('行驶的里程数：', round(ref_total_distance, 4))
print('行驶的里程误差：', round(ref_total_distance - test_total_distance, 4))
print('定位误差最大值:', round(max(data_detail_final), 4))
print('速度误差最大值:', round(max(data_speed_final), 4))
print('高程误差最大值:', round(max(data_high_final), 4))
print('速度误差最大值:', round(max(data_speed_final), 4))
print('定位误差最小值:', round(min(data_detail_final), 4))
print('速度误差最小值:', round(min(data_speed_final), 4))
print('高程误差最小值:', round(min(data_high_final), 4))
print('定位误差平均值:', round(sum(data_detail_final)/len(data_detail_final), 4))
print('速度误差平均值:', round(sum(data_speed_final)/len(data_speed_final), 4))
print('高程误差平均值:', round(sum(data_high_final)/len(data_high_final), 4))
print('定位误差标准差:', round(math.sqrt(sum(list(map(lambda x: x**2, data_detail_final))) / (len(data_detail_final)-1)), 4))
print('速度误差标准差:', round(math.sqrt(sum(list(map(lambda x: x**2, data_speed_final))) / (len(data_speed_final)-1)), 4))
print('高程误差标准差:', round(math.sqrt(sum(list(map(lambda x: x**2, data_high_final))) / (len(data_high_final)-1)), 4))

y1 = data_detail_final
y2 = data_speed_final
y3 = data_high_final
x1 = range(len(y1))
x2 = range(len(y2))
x3 = range(len(y3))
plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.show()
