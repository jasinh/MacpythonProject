from name_fuction import get_formatted_name
print('请输入姓名，按q退出')
while True:

    first=input('请输入你姓：')
    if first == 'q':
        break
    last=input('请输入名：')
    if last == 'q':
        break
    print('得到格式化的名字：',get_formatted_name(first,last))


