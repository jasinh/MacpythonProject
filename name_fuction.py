def get_formatted_name(first,last):
    """生成格式化的兔子"""
    full_name=f'{first} {last}'
    print(__name__)
    return full_name.title()
if __name__ =='__main__':
    print('now in myself running')
print(get_formatted_name('huang','jiaxing'))