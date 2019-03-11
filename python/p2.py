def main():
    arr1=(1,2,3,4,5,6)
    print(type(arr1),arr1)

    arr2=[1,2,3,4,5]
    arr2.append(8)
    arr2.insert(0,23)
    arr2.insert(-1,99)
    arr2.append(101)
    arr2.insert(-2,69)
    print(type(arr2),arr2)

main()
