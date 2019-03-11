def main():
    a,b=1,1
    while a < 100 or b < 100:
        print(a," ",b," ")
        a=a+b
        b=a+b
    print(" subtraction is ",5-3)
    print(" addtion is ",5+3)
    print(" multiplication is ",5*3)
    print(" divison is ",5/3)
    print(" modulo is ",5%3)
    x,y= divmod(12,5)
    print(" divmod(12,5) ",x,y)

    print(5 < 3)
    print(5 > 3)
    print(5 <= 3)
    print(5 >=3)
    print(5 == 3)
    print(5 != 3)
    x,y=5,6
    print(x is y)
    print(x is not y)
    print(id(x)," ",id(y))
    y=5
    print(id(x)," ",id(y))
main()
