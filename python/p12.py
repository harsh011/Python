class c1:
    def __init__(self):
        print("object constructed")
    def method1(self):
        print(" method 1 from class 1")
    def method2(self):
        print("method2 from class 1")
        
def main():
    obj1 = c1()
    obj1.method1()
    obj1.method2()

main()
