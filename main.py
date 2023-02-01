board = [" " for x in range(9)] # inicializa o tabuleiro com 9 espaços vazios


def print_board():
    # construção das linhas do tabuleiro
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    # impressão do tabuleiro
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon):
    # determina o número do jogador a partir do ícone da jogada
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    # verifica se a casa escolhida já está preenchida
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")


def is_victory(icon):
    # verifica se as condições de vitória foram atendidas
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    # verifica se houve empate (todas as casas preenchidas sem vitória)
    if " " not in board:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move("O")
        if is_victory("O"):
            print_board()
            print("O wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
