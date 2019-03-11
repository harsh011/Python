class c1:
    def __init__(self,value=12):
        self._v1 = value
        print("object constructed ()".format(self._v1))
    def method1(self):
        print(" method 1 from class 1",self._v1)
    def method2(self):
        print("method2 from class 1")
        
def main():
    obj1 = c1(34)
    obj1.method1()
    obj1.method2()
    obj1._v1 = 11
    obj1.method1()

main()
