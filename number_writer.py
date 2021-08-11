import json
numbers=[2,3,5,7,11,13]
filename='number.jason'
with open(filename,'w') as fileobject:
    json.dump(numbers,fileobject)
with open(filename,'r') as fileobject:
    print(fileobject.read())