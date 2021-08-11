filename='pi_digits.txt'
join_pi=''
with open(filename) as file_object:
    for line in file_object:
        join_pi+=line.strip().replace(' ','')
    print(join_pi)
    print(f'该文件一共{len(join_pi)}位')




