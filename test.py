import openpyxl
import numpy as np
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', password='ll891119', port=3306, db='furthereast')
# 建立游标
cur = conn.cursor()
# 载入excel表格
wb = openpyxl.load_workbook('test.xlsx')
sh = wb['Sheet1']
department = []
# 按行取数
for case in list(sh.rows)[1:]:
	# 读取所有部门
	if case[7].value not in department:
		department.append(case[7].value)
# 部门录入数据库
for case in department:
	cur.execute("""INSERT INTO TEST(Department) VALUES (%s)""" % (case))
# print(department)

num = [0] * len(department)
d1 = {}
d2 = {}
# 创建两个空字典列表
for i in range(len(department)):
	d1[department[i]] = num[i]
	d2[department[i]] = num[i]
# print(d1)

for case in list(sh.rows)[1:]:
	# 实际产生业务
	if case[53].value == '是':
		d1[case[7].value] += 1
		# 是否使用包车
		if case[15].value == '是':
			d2[case[7].value] += 1
print(d1)
print(d2)




# data = []
# message = []
# num = 0
# for case in list(sh.rows)[1:]:
# 	message = [case[7].value, case[10].value, case[15].value, 0, 0]
# 	# value = case.value
# 	# if value not in department:
# 	# 	department.append(value)
# 	data.append(message)
# print(len(data))
# print(np.array(data).reshape(len(data), 5))


