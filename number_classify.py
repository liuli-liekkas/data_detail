import openpyxl
work_sheet = 'd:/files/python数据文件/物流费用运输台账 六家/物流费用运输台账 温州200101-0926.xlsx'
wb = openpyxl.load_workbook(work_sheet)
sheet_old = wb['原表']
sheet_names = wb.get_sheet_names()
print(sheet_names)
if '新表' not in sheet_names:
    wb.create_sheet('新表')
sheet_new = wb['新表']
case_one = []

for case in list(sheet_old.rows)[1:]:
    for num_one in range(len(case)):
        case_one.append(case[num_one].value)
    print(case_one)
    if case_one[17]:
        equip_num = case_one[17].split(',')
        for num in range(len(equip_num)):
            if len(case_one) == 62:
                case_one.append(equip_num[num])
            else:
                case_one[62] = equip_num[num]
            print(case_one)
            sheet_new.append(case_one)
    case_one = []


wb.save(work_sheet)
