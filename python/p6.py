def main():
    x,y=5,6
    print(x is y)
    print(x is not y)
    print(id(x)," ",id(y))
    y=5
    print(id(x)," ",id(y))
main()
