def emogi_decorator(func):
    def wrapper(name):
        func(name)
        print('^^//')
    
    return wrapper

@emogi_decorator
def ko_hello(name):
    print(f'안녕하세요 {name}님')

ko_hello('냥냥')
