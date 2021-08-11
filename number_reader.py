import json
filename='number.jason'
with open(filename) as file_object:
   numbers=json.load(file_object)
print(numbers)