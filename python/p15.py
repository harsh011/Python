class superduck:
    def __init__(self,**kwargs):
        self.variables = kwargs
        print("object constructed ()")

    def setva1(self,varname,varvalue):
        self.variables[varname]=varvalue

    def getvalue(self,varname):
        return (self.variables.get(varname,None))
        
def main():
   
    d2 = superduck(feet=3,color='white',feather='black')
    print(d2.getvalue('feet'))
    print(d2.getvalue('color'))
    print(d2.getvalue('feather'))

    d3 = superduck(feet=3,color='white',feather='black',eye='black',walk=True)
    d3.setval('color','blue')
    print(d3.getvalue('feet'))
    print(d3.getvalue('color'))
    print(d3.getvalue('feather'))
    print(d3.getvalue('eye'))
    print(d3.getvalue('walk'))
if  __name__ == "__main__": main()
