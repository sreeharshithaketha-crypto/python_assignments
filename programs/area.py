class Area:
    def calculate(self, a,b,r):
        if b is None and a is True:
            print("Area of Square:", a * a)
            print("Area of Circle:", 3.14 * r * r)
        else:
            print("Area of Rectangle:", a * b)

obj = Area()
obj.calculate(5,3,7)
obj.calculate(5,10)