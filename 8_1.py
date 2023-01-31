class Point:#점(Point)
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

#직사각형(Rectangle)
class Rectangle:
    def __init__(self,position=Point(0,0),width=0,height=0):
        self.position = position
        self.width = width
        self.height = height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return (self.width + self.height)*2
    def is_square(self):
        if self.width == self.height:
            print('True')
        else:
            print('False')

rectangle = Rectangle()
rectangle.position = Point(3,4)
rectangle.width =20
rectangle.height=40
print("면적:",rectangle.get_area())

point = Point(10,10)
rect1 = Rectangle(point,20,30)
print("x:",rect1.position.x)
print("y:",rect1.position.y)
print("width:",rect1.width)
print("height:",rect1.height)
print("면적:",rect1.get_area())
print("둘레:",rect1.get_perimeter())
print("정사각형 유무:",rect1.is_square)

-----------------------------------------------
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, po1, po2):
        self.p1 = po1
        self.p2 = po2
    
    #instance method로 입력은 없고 면적을 리턴
    def get_area(self):
        width = abs(self.po1.x - self.po2.x)
        height = abs(self.po1.y - self.po2.y)
        # po1 = self.p1
        # po2 = self.p2
        # area = abs(po1.x - po2.x)*abs(po1.y - po2.y) 
        return width*height
    
    def get_perimeter(self):
        return (self.width + self.height)*2
    
    def get_perimeter(self):
        return (self.width + self.height)*2
    def is_square(self):
        if self.width == self.height:
            print('True')
        else:
            print('False')


p1 = point(1,3)
print(p1.x) #p1의 x좌표 출력
p2 = point(3,1)
print(p2.x,p2.y)
r1 = Rectangle(p1,p2)
print(r1.get_area())