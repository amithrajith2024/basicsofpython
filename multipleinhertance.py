class Demo1:
    x="hi"
    def display(self):
        print(self.x," Python")

class Demo2:
    y=4
    z=9
    def sum(self):
        print(self.y+self.z)

class ChildClass(Demo1,Demo2):
    def data(self):
        print(" Display all ")

obj=ChildClass()
obj.display()
obj.sum()
    