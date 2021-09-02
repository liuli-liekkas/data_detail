import os.path
import math


# 经典两点计算公式
def geo_distance(lng_test, lat_test):
    lng_test = round(lng_test // 100 + lng_test % 100 / 60, 6)
    lat_test = round(lat_test // 100 + lat_test % 100 / 60, 6)
    lng_ref = 11.5
    lat_ref = 48.25
    # lng_ref = 121.18034
    # lat_ref = 31.28351
    # 角度转弧度
    lng1, lat1, lng2, lat2 = map(math.radians, [lng_test, lat_test, lng_ref, lat_ref])
    d_lng = lng2 - lng1
    d_lat = lat2 - lat1
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lng / 2) ** 2
    dis = 2 * math.asin(math.sqrt(a)) * 6371 * 1000
    return dis


# 数据格式化
filename_test = 'gnss/test20210816/测试数据汇总/CASE2/单伽利略/CASE2_GA_DUT.txt'
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

# 录入测试数据_静态点
with open(filename_test, 'r', encoding='utf-8') as file_test:
    data_test = file_test.readlines()
    num = len(data_test)
# TEST_GPRMC
for line in range(num):
    data_test_split = data_test[line].split(',')
    if data_test_split[0] == '$GPRMC':
        if data_test_split[5]:
            distance = geo_distance(float(data_test_split[5]), float(data_test_split[3]))
            print(data_test_split[8])
            data_detail_final.append(distance)

print('定位误差最大值:', round(max(data_detail_final), 4))
print('定位误差最小值:', round(min(data_detail_final), 4))
print('定位误差平均值:', round(sum(data_detail_final)/len(data_detail_final), 4))
print('定位误差标准差:', round(math.sqrt(sum(list(map(lambda x: x**2, data_detail_final))) / (len(data_detail_final)-1)), 4))

