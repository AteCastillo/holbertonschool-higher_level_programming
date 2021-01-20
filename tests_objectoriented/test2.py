class Person:
    def __init__(self, name):
        self.name = name
    def hi(self):
        print('hey, my name is', self.name)
p = Person('Swaroop')
p.hi()
    