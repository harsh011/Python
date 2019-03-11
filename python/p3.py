def main():
    s1="this is \n string"
    print(s1)
    s2=r"this is \n string\n\n " 
    print(s2)
    x=13
    s3=r"this is {} string".format(x)
    print(s3)
    s4=" string 1 " " string 2"
    print(s4)
    s5='''this is string
this is second line
this is third line'''
    print(s5)
    print('{0: ^11}'.format('hello'))
    print('{0:#^13}'.format('hello'))
    print('{0:*^9}'.format('hello'))
    print('{0:@^8}'.format('hello'))
    x=5
    print(type(x))
    x=str(x)
    print(type(x))
main()
    
