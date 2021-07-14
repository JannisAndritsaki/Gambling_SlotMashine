#This is the main
def WelcomeScreen():
    print("---------------------------------------------------------------")
    print("Welcome to the CASINO. Have fun and go win some money.")
    print("---------------------------------------------------------------")


def Hello():
    print("hello")

def Tschuess():
    print("hau ab")

def StartGame(user_input):
    if user_input == "yes":
        Hello()
        return 1

    if user_input == "no":
        Tschuess()
        return 0

    else:
        return 0


def Start_Gambling():
    print("Do you want to start?")
    print("Type -yes-  or  -no-")
    start_game = input("-> ")
    StartGame(start_game)




if __name__ == "__main__":
    WelcomeScreen()
    Start_Gambling()
