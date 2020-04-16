import openpyxl
import numpy as np

wb = openpyxl.load_workbook('test.xlsx')
sh = wb['Sheet1']
sh = []
department = []
for case in list(sh.rows)[1:]:
	if case[7].value not in department:
		department.append(case[7].value)
# print(department)

num = [0] * len(department)
d1 = {}
d2 = {}
for i in range(len(department)):
	d1[department[i]] = num[i]
	d2[department[i]] = num[i]
# print(d1)

for case in list(sh.rows)[1:]:
	if case[53].value == '是':
		d1[case[7].value] += 1
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


