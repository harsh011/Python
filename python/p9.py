def main():
    
    try:
        fh = open("abc.txt")
    except IOError:
        print("error in openning file");
    else:
            for line in fh:
                print(line.strip())
main()
