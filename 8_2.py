class Stack:
    def __init__(self):
        self.items = []
    
    def empty(self):
        return not self.items

    def pop(self,item):
        return self.items.pop
    
    def push(self,item):
        self.items.append(item)

    def __repr__:
    
s = Stack()
print(s)
l =list()
print(l)
nums = len(l)

s = list()
repr(s)

built함수
len() => __len__
print() => __str__
repr() => __repr__


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod()
    def get_age(cls,name, year):
        age =
        return  cls(name,age)
        
    

person1 = Person('Mark',20)
person2 = Person('Mark',20)