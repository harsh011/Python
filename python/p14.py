class duck:
    def __init__(self,**kwargs):
        self.variables = kwargs
        print("object constructed ()")

    def setva1(self,color):
        self.variables['color']=color

    def getval(self):
        return (self.variables.get('color',None))
        
def main():
    d1 = duck(color='Green')
    print(d1.getval())
    d1 = duck(color='red')
    print(d1.getval())

main()
