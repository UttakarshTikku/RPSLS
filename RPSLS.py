from Utils import Choice

def promptForInput(a):
    print("Player ", a, " Select From Following : ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Lizard")
    print("5. Spock")
    return int(input("Choice : "))

def classifyResult(a):
    if a == (Choice.ROCK,Choice.PAPER) or a == (Choice.PAPER,Choice.ROCK):
        print("Paper wraps Rock")
        return a.index(Choice.PAPER) + 1
    if a == (Choice.ROCK,Choice.SCISSORS) or a == (Choice.SCISSORS,Choice.ROCK):
        print("Rock crushes Scissors")
        return a.index(Choice.ROCK) + 1
    if a == (Choice.ROCK,Choice.LIZARD) or a == (Choice.LIZARD,Choice.ROCK):
        print("Rock crushes Lizard")
        return a.index(Choice.ROCK) + 1
    if a == (Choice.ROCK,Choice.SPOCK) or a == (Choice.SPOCK,Choice.ROCK):
        print("Spock vaporizes Rock")
        return a.index(Choice.SPOCK) + 1
    if a == (Choice.PAPER,Choice.SCISSORS) or a == (Choice.SCISSORS,Choice.PAPER):
        print("Scissors cuts Paper")
        return a.index(Choice.SCISSORS) + 1
    if a == (Choice.PAPER,Choice.LIZARD) or a == (Choice.LIZARD,Choice.PAPER):
        print("Lizard eats Paper")
        return a.index(Choice.LIZARD) + 1
    if a == (Choice.PAPER,Choice.SPOCK) or a == (Choice.SPOCK,Choice.PAPER):
        print("Paper disproves Spock")
        return a.index(Choice.PAPER) + 1
    if a == (Choice.SCISSORS,Choice.LIZARD) or a == (Choice.LIZARD,Choice.SCISSORS):
        print("Scissors decapitates Lizard")
        return a.index(Choice.SCISSORS) + 1
    if a == (Choice.SCISSORS,Choice.SPOCK) or a == (Choice.SPOCK,Choice.SCISSORS):
        print("Spock smashes Scissors")
        return a.index(Choice.SPOCK) + 1
    if a == (Choice.LIZARD,Choice.SPOCK) or a == (Choice.SPOCK,Choice.LIZARD):
        print("Lizard poisons Spock")
        return a.index(Choice.LIZARD) + 1

def gameInstance(p1_choice, p2_choice):
    if p1_choice == p2_choice :
        print("Draw")
    else:
        print( "Player ", classifyResult((p1_choice, p2_choice)), " Wins!")

x1 = Choice(promptForInput(1))
x2 = Choice(promptForInput(2))
gameInstance(x1, x2)