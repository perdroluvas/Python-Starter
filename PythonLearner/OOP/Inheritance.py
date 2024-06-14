class Parent:
    parentAttr=100
    def __init__(self):
        print("instantiating parent")
    def parentMethod(self):
        print('parent method')
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("parent attribute: ", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("instantiating child")
    def childMethod(self):
        print('child method')
    def getAttr(self):
        super().getAttr()#super = getattr from PARENT

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr
print(c.parentAttr)

p = Parent()
p.parentMethod()
p.getAttr()
p.setAttr(300)
print(p.parentAttr)
