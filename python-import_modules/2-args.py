#!/usr/bin/python3
argv = []
x = len(argv) - 1
if x == 0:
    print("0 arguments.")
elif x == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(x))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
if __name__ == "__main__":
    main()
