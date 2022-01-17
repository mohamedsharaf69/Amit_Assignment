def calculator():
    while True:
        fn = int(input("Enter First Number\n"))
        sn = int(input("Enter Second Number\n"))
        t = input("Enter type of calculation\n")
        #if to add 2 numbers
        if t == "add":
            out = fn+sn
        #if to subtract 2 numbers
        elif t == "sub":
            out = fn-sn
        #if to multiply 2 numbers
        elif t == "mult":
            out = fn * sn
        # if to divide 2 numbers
        elif t == 'div':
            out = fn / sn
        print(out)
        an = input("Do you wnat another operation?")
        #if condition to keep the loop going until the the user answers another word than yes
        if an == 'yes':
            continue
        else:
            break