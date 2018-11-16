import RPSLS

def chooseMode():
    print("Select Game Mode : ")
    print("1. Human vs Human")
    print("2. Human vs AI")
    print("3. AI vs AI")
    print("Anything Else To Exit")
    return int(input("Choice : "))

while True:
    print("--------------------------------------------------------------------------------------------")
    mode = chooseMode()
    if mode > 3 or mode < 1 :
        break
    if mode == 1:
        while True:
            RPSLS.gameInstance( RPSLS.promptForInput(1), RPSLS.promptForInput(2))
            again = input("Play again? (Yy/Nn)")
            if "N" in again or "n" in again:
                break
            print("***************************************************")
    elif mode == 2:
        print("Pick AI agent : ")
        agent = None
        while True:
            RPSLS.gameInstance( agent.promptForInput(1), RPSLS.promptForInput(2))
            again = input("Play again? (Yy/Nn)")
            if "N" in again or "n" in again:
                break
            print("***************************************************")
    elif mode == 3:
        print("Pick AI agent 1 : ")
        agent1 = None
        print("Pick AI agent 2 : ")
        agent2 = None
        while True:
            RPSLS.gameInstance( agent1.promptForInput(1), agent2.promptForInput(2))
            again = input("Play again? (Yy/Nn)")
            if "N" in again or "n" in again:
                break
            print("***************************************************")