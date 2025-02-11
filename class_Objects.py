class PointCloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        print("Moving the point cloud...")

    def draw(self):
        print("Drawing the point cloud...")

point1 = PointCloud(10, 20)

# point1.x = 10
# point1.y = 20
point1.draw()
print(point1.x, point1.y)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Person is talking to... {self.name}')
    
john = Person("John Smith")

john.talk()