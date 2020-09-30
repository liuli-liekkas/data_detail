import openpyxl
wb = openpyxl.load_workbook('d:/files/python数据文件/物流费用运输台账 六家/物流费用运输台账 宁波200101-0926.xlsx')
sheet_old = wb['原表']
sheet_names = wb.get_sheet_names()
print(sheet_names)
if '新表' not in sheet_names:
    wb.create_sheet('新表')
sheet_new = wb['新表']

# for case in list(sheet_old.rows)[2:]:
#     print(len(case))
#     for num in range(len(case)):
#         print(data.value)

wb.save('d:/files/python数据文件/物流费用运输台账 六家/物流费用运输台账 宁波200101-0926.xlsx')
