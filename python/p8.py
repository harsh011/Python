def main():
    fh = open("harsh.txt")
    for line in fh:
        print(line.strip())

    try:
        fh = open("abc.txt")
    except:
        print("error in openning file");
    else:
            for line in fh:
                print(line.strip())
main()
