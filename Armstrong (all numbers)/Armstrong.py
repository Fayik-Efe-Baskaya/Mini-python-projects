def armstrong():
    print("-"*50)
    print("Welcome to the armstrong calculator!")
    print("-"*50)

    while True:
        def control():
            while True:
                c = input("Press x to exit or press ENTER to continue: ").lower()
                if c == "":
                    return True
                elif c == "x":
                    return False
                else:
                    continue

        control = control()
        if control == False:
            print("The program is closing...")
            return

        def get_number():
            while True:
                try:
                    x = int(input("Please enter the integer: "))
                    return x

                except ValueError:
                    print("Please enter an integer!\n")
                    continue

                except TypeError:
                    print("Please enter an integer!\n")
                    continue

        num = get_number()


        def isarmstrong(number):
            total = 0
            number = str(number)

            for i in range(len(number)):
                total += int(number[i]) ** int(len(str(number)))

            if total == int(number):
                print(f"{number} is an armstrong number.\n")
            else:
                print(f"{number} is NOT an armstrong number.\n")

        isarmstrong(num)


armstrong()


