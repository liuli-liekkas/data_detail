# 数据格式化
import os.path


# .dat文件改为.txt
def change_name():
    files = os.listdir(path1)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == '.dat':
            new_name = portion[0] + '.txt'
            os.chdir(path1)
            os.rename(filename, new_name)


def change_standard():
    with open('12-123-Ref.txt', 'r') as file_default:
        data_default = file_default.readlines()
        for line in data_default:
            new_message = line.split(',')
            if new_message[0] == '$GARMC':
                new_message[1] = new_message[1] + ',' + 'A'
                new_message_detail = ','.join(new_message)
                print(new_message_detail)


def delete_ending():
    new_data = []
    second_data = ''
    with open('./gnss/test20210622/test20210622.txt') as file_default:
        data_default = file_default.readlines()
        for line in data_default:
            line = line[0:-1]
            new_data.append(line)
        for num in range(len(new_data)):
            second_data = second_data + new_data[num]
        # num = len(second_data)
        # print(num)
        third_data = second_data.split('$')

    with open('./gnss/test20210622/test20210622_detail.txt','w+') as file:
        for line in third_data:
            file.write(line + '\n')


if __name__ == '__main__':
    delete_ending()
