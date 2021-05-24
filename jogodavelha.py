def menu():

    jogar = 1
    while jogar:
        print("Insira 1 para jogar \n"
              "---*---*---*---*---")

        jogar = int(input("Opção: "))

        if jogar:
            game()

def game():

    jogada = 0
    while ganhou() == 0:
        print("\nVez do jogador ", jogada % 2 + 1)
        exibe()

        linha = int(input("\nInsira a linha você vai jogar: "))
        coluna = int(input("Insira coluna você vai jogar: :"))

        if board[linha - 1][coluna - 1] == 0:

            if (jogada % 2 + 1) == 1:
                board[linha - 1][coluna - 1] = 1

            else:
                board[linha - 1][coluna - 1] = -1

        else:
            print("Seu apedeuda, aqui não está vazio!")
            jogada -= 1

        if ganhou():
            print("\nParabéns APEDEUTA!  ", jogada % 2 + 1, " ganhou depois de ", jogada + 1, " rodadas! \n")
            print("Parabéns!!! \n")

        jogada += 1

def ganhou():

    for i in range(3):
        soma = board[i][0] + board[i][1] + board[i][2]

        if soma == 3 or soma == -3:
            return 1

    for i in range(3):
        soma = board[0][i] + board[1][i] + board[2][i]

        if soma == 3 or soma == -3:
            return 1

    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]

    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0

def exibe():

    for i in range(3):
        for j in range(3):

            if board[i][j] == 0:
                print(" _ ", end=' ')

            elif board[i][j] == 1:
                print(" X ", end=' ')

            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

menu()