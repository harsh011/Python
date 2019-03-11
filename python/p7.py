def main():
    l1=[1,2,3,4,5,6,7]
    print(l1[0])
    print(l1[0:5])

    print("\n\n output of slicing")
    l1[:] = range(1,101)
    print(l1[0:50])
    print(l1[6:100:3])

    #for i in l2[0:100:2]:
     #   print(i,end='@')
main()
