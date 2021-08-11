write_filename='programming.txt'
with open(write_filename,'w') as file_object:
    file_object.write('I love programming\n')
    file_object.write('I love play game\n')
with open(write_filename) as file_object:
    for line in file_object:
        print(line.strip())