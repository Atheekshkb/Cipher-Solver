class Student:
    def __init__(self, name='someone', major = '', age=0):
        self.name = name
        self.major = major
        self.age = age
        return       
    def set_name(self, name):
        self.name = name
        return
    def set_major(self, major):
        self.major = major
        return
    def set_age(self, age):
        self.age = age
        return 
    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def get_age(self):
        return self.age
    def __lt__(self, obj2):
        if type(self) == type(obj2):
            if self.age > obj2.age: return True
            else: return False
        else: return None
    def __str__(self):
        return (f"{self.name} is {self.age} years old. \n{self.name}'s major is {self.major}.")
if __name__ == '__main__':
    alice = Student("Alice Wood", "economics" , 19)
    print(alice)
    alex = Student()
    alex.set_name("Alex Green")
    alex.set_major("chemistry")
    alex.set_age(18)
    print(alex)
    if alice > alex:print(f'{alex.get_name()} is older than {alice.get_name()}.')
    else: print(f'{alex.get_name()} is not older than {alice.get_name()}.')