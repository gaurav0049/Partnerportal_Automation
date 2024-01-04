class Name:
    variable=10
    def __init__(self):
        pass

    def variable2(self):
        self.variable2=20
        return  (self.variable2+Name.variable)


class Adjust:
    obj1 = Name()
    variable1=obj1.variable2()
    def Pass(self):
        return Adjust.variable1
obj=Adjust()
print(obj.Pass())
