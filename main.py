# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f'{self.name} is siting')
    def roll_over(self):
        print(f'{self.name} rolled over!')
dog1=Dog('hjx',5)
print(f"my dog' name is {dog1.name}")
print(f'my dog is {dog1.age} years old')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
