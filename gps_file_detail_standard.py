# 数据格式化
# files = os.listdir(path1)
# for filename in files:
#     portion = os.path.splitext(filename)
#     if portion[1] == '.dat':
#         new_name = portion[0] + '.txt'
#         os.chdir(path1)
#         os.rename(filename, new_name)

# os.chdir(path1)
# with open('0727-dynamic-comb.txt', 'r') as file_default:
#     data_default = file_default.readlines()
#     print(data_default)
#     for line in data_default:
#         new_message = line.split(',')
#         if new_message[0] == '$GARMC':
#             new_message[1] = new_message[1] + ',' + 'A'
#             # print(new_message)
#             new_message_detail = ','.join(new_message)
#             print(new_message_detail)