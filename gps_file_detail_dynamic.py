import os.path
import numpy as np
import math


# 经典两点计算公式
def geo_distance(lng_test, lat_test, lng_default, lat_default):
    lng_test = round(lng_test // 100 + lng_test % 100 / 60, 6)
    lat_test = round(lat_test // 100 + lat_test % 100 / 60, 6)
    lng_default = round(lng_default // 100 + lng_default % 100 / 60, 6)
    lat_default = round(lat_default // 100 + lat_default % 100 / 60, 6)
    lng1, lat1, lng2, lat2 = map(math.radians, [lng_test, lat_test, lng_default, lat_default])  # 角度转弧度
    d_lng = lng2 - lng1
    d_lat = lat2 - lat1
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lng / 2) ** 2
    dis = 2 * math.asin(math.sqrt(a)) * 6371 * 1000
    print(dis)
    return dis

# 三点计算公式
# def geodistance(lng_test, lat_test, h_test, lng_default, lat_default, h_default):
#     lng_test, lat_test, lng_default, lat_default = map(math.radians, [lng_test, lat_test, lng_default, lat_default])
#     delta_x = h_test * math.cos(lat_test) * math.cos(lng_test) - h_test * math.cos(lat_default) * math.cos(lng_default)
#     delta_y = h_test * math.cos(lat_test) * math.sin(lng_test) - h_test * math.cos(lat_default) * math.sin(lng_default)
#     delta_z = h_test - h_default
#     dis = math.sqrt(delta_x + delta_y + delta_z)
#     return dis



path1 = "e:/LEAR_GNSS_Test/Comb"



os.chdir(path1)
data_test_detail = {}
distance_get = []
with open('QCOM_LOG.txt', 'r') as file_test:
    data_test = file_test.readlines()
    num_test = len(data_test)
    data_test_temporary = []
    for line in range(num_test):
        data_test_temporary = data_test[line].split(',')
        if data_test_temporary[0] == '$GPRMC':
            if data_test_temporary[3]:
                data_test_detail[data_test_temporary[1].split('.')[0]] = [data_test_temporary[3], data_test_temporary[5]]
    print(data_test_detail)

data_default_detail = {}
with open('0727-dynamic-comb.txt', 'r') as file_default:
    data_default = file_default.readlines()
    num_default = len(data_default)
    data_default_temporary = []
    for line in range(num_default):
        data_default_temporary = data_default[line].split(',')
        if data_default_temporary[0] == '$GARMC':
            if data_default_temporary[3]:
                data_default_detail[data_default_temporary[1].split('.')[0]] = [data_default_temporary[2], data_default_temporary[4]]
    print(data_default_detail)

for key in data_test_detail:
    print(key)
    print(data_test_detail[key])
    print(data_default_detail[key])
    distance = geo_distance(float(data_test_detail[key][1]), float(data_test_detail[key][0]), float(data_default_detail[key][1]), float(data_default_detail[key][0]))
    distance_get.append(distance)

print('最大值:', max(distance_get))
print('最大值:', min(distance_get))
print('平均值:', sum(distance_get)/len(distance_get))
print(distance_get)
print(math.sqrt(sum(list(map(lambda x: x**2, distance_get))) / (len(distance_get)-1)))

print(len(distance_get))

geo_distance(12.9983215, 50.03123, 12.99837, 50.03112)
# files = os.listdir(path1)
# os.chdir(path1)
# data_gnrmc = []
# data_gngga = []
# data_test = []
# lng_default = 13
# lat_default = 50
# h_default = 50
# distance_final = 0
# n = 0
# for filename in files:
#     with open(filename, 'r') as file:
#         data = file.readlines()
#         num = len(data)
#     for line in range(num):
#         if data[line].split(',')[0] == '$GPRMC':
#             data_gnrmc.append(data[line])
#             if data[line].split(',')[3]:
#                 # print(float(data[line].split(',')[3]))
#                 # print(float(data[line].split(',')[5]))
#                 distance = geo_distance(float(data[line].split(',')[5]), float(data[line].split(',')[3]), lng_default, lat_default)
#                 # print(distance, data[line].split(',')[1])
#                 # print(distance_final, data[line].split(',')[1])
#                 if distance_final == 0:
#                     distance_final = distance
#                 else:
#                     distance_final = distance_final + distance
#                 n += 1
#                 print(distance_final / n, n, data[line].split(',')[1], '\n')
#             else:
#                 distance_final = 0
#                 n = 0
#                 print('hello')
        # if data[line].split(',')[0] == '$GNGGA':
        #     data_gngga.append(data[line])
        # for num in range(len(data_gnrmc)):
        #     for i in range(10):
        #         if data_gnrmc[num + i].split(',')[3] and data_gngga[num + i].split(',')[9]:
        #             data_test.append(data_gnrmc[num + i].split(',')[3])
        #             data_test.append(data_gnrmc[num + i].split(',')[5])
        #             data_test.append(data_gnrmc[num + i].split(',')[7])
        #             data_test.append(data_gngga[num + i].split(',')[9])
        #     if len(data_test) == 40:
        #         data_test = np.array(list(map(float, data_test))).reshape(4, 10)
        #         lng_test = math.floor(data_test.sum(axis=1)[1] / 1000) + (
        #                     data_test.sum(axis=1)[1] / 1000 - math.floor(data_test.sum(axis=1)[1] / 1000)) / 0.6
        #         lat_test = math.floor(data_test.sum(axis=1)[0] / 1000) + (
        #                     data_test.sum(axis=1)[0] / 1000 - math.floor(data_test.sum(axis=1)[0] / 1000)) / 0.6
        #         h_test = data_test.sum(axis=1)[3]
        #         if geodistance(lng_test, lat_test, h_test, lng_default, lat_default, h_default) > 100:
        #             data_test = []
        #             continue
        #         else:
        #             print("定位误差为:", geodistance(lng_test, lat_test, h_test, lng_default, lat_default, h_default))
        #             print("定位时间为:", num, "秒")
        #             break
        #     else:
        #         data_test = []
    # print(data_gnrmc)
    # print(len(data_gnrmc))


