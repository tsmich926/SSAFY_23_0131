def ko_hello(name):
    print(f'안녕하세요 {name}님')

def en_hello(name):
    print(f'hello {name}님')

def emoji_hello(name):
    print(f'안녕하세요 {name}님')
    print('^^//')

print(ko_hello('이름'))

def add_emogi(name, func):
    func(name)
    print('^~^')
add_emogi('aiden', ko_hello)
add_emogi('aiden',ko_hello)

# new_func = emogi_decorator(ko_hello)
# new_func('auend')
emogi_decorator(en_hello)('aaiden')



def emogi_decorator(func):
    def wrapper(name):
        func(name)
        print('^^//')
    
    return wrapper

@emofi_decorator
def ko_hello(name):
    print(f'안녕하세요 {name}님')

ko_hello('냥냥')

class MyClass:
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'statuc method'
    
    my_class = MyClass()
    print(my_class.method())
    print(my_class.classmethod())
    print(my_class.staticmethod())
    
    #상속
    class person:
        def __init__(self,name,age)
            
    isinstance(object,classinfo)
    # subclass인 경우에도 true가 나옴
    issubclass(class,classinfo)
    # classinfo의 모든 항목을 검사

    super()
    #자식클래스에서 부모클래스 사용

#같은 이름이지만 동작이 다름
#?다형성

class Person:
    def __init__(self,name,age)
        self.name = name
    def talk(self):
        print(f'반가워{self.name}')

class Professor(Person):
    def talk(self):
        print(f'{self.name}일세')
        #재정의 오버라이딩

class student(Person):
    def talk(self):
        super().talk() #상위 클래스의 무언가를 특정
        print(f'저는 학생임')

#?캡슐화
#protected
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        return self._age

    def set_age(age):
        self._age = age #메서드를 통한 접근과 값변경

    #private
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def get_age(self):
    return self.__age 

class Person:
    def __init__(self):
        self._age = 0 #private
    @property
    def age(self): #getter
        print('getter 호출')
        return self._age
    @age.setter
    def age(self.age): #setter
        print('setter 호출')
        self._age = age

    ##age = property(get_age, set_age) 

p1 = Person()
# p1._age = 25 #이거 안됨
# print(p1._age) #이거 안됨

p1.set_age(25)
print(p1.get_age()) #불편

p1 = Person()
p1.age = 25
print(p1.age)

