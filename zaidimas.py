import random
import time

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

print("Čia kryžiukų ir nuliukų žaidimas!")
print("Žaidėjas [X] --- Kompiuteris  [O]\n")
print()
print()
print("Prašome palaukti...")
time.sleep(3)
print()
print()

# Žaidimo lenta
def Lenta(board):
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("___|_____|___")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("___|_____|___")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])


# Ėjimas
def Ejimas(board):
    inp = int(input("Pasirinkti langelį 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Langelis užimtas.Pasirinkti kitą.")



# Tikrinimas ar laimėjo
def Horizontaliai(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def Vertikaliai(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def Istrizaine(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def Laimejimas(board):
    global gameRunning
    if Horizontaliai(board):
        Lenta(board)
        print(f"Laimėtojas {winner}!")
        gameRunning = False

    elif Vertikaliai(board):
        Lenta(board)
        print(f"Laimėtojas {winner}!")
        gameRunning = False

    elif Istrizaine(board):
        Lenta(board)
        print(f"Laimėtojas {winner}!")
        gameRunning = False


def Lygiosios(board):
    global gameRunning
    if "-" not in board:
        Lenta(board)
        print("Niekas nelaimėjo!")
        gameRunning = False


# Kitas žaidėjas
def kitasZaidejas():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def Kompiuteris(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            kitasZaidejas()


while gameRunning:
    Lenta(board)
    Ejimas(board)
    Laimejimas(board)
    Lygiosios(board)
    kitasZaidejas()
    Kompiuteris(board)
    Laimejimas(board)
    Lygiosios(board)




