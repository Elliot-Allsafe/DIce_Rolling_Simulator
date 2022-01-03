import random
import sys


def run():
    a = [0]

    try:
        while True:
            inp_ut = str(input("> "))
            if inp_ut == "":
                number = random.randint(1, 6)
                print(number)
                a.append(number)
            elif inp_ut == "R" or inp_ut == "r":
                if len(a) < 2:
                    print("Please Roll the Dice First..")
                else:
                    print(a[1:])
            elif inp_ut == "C" or inp_ut == "c":
                a = [0]
                continue
            elif inp_ut == "Q" or inp_ut == "q":
                print("Exiting!")
                a = [0]
                break
            else:
                print("Read the Instructions Carefully:")
                print("Press Enter to Roll The Dice.")
                print("Enter R/r for all results..")
                print("Enter C/c to clear History Rolls.")
                print("Enter Q/q to Exit at any time.")
                continue
    except ValueError:
        print("Press Enter Only. or q/Q to exit..")
        a = [0]
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting Program")
        a = [0]
        sys.exit()
