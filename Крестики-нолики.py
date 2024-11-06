def print_board(board):
    """Функция для вывода игрового поля."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Разделитель между рядами


def check_winner(board):
    """Функция для проверки на наличие победителя."""
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    """Функция для проверки заполненности поля."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # Если нашли хотя бы одну пустую клетку
    return True  # Если пустых клеток нет


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Создаем пустое поле
    current_player = "X"  # Начинаем с игрока X

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите строку (0-2): "))
        col = int(input(f"Игрок {current_player}, введите столбец (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player  # Делаем ход
        else:
            print("Эта клетка уже занята! Попробуйте снова.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Поздравляем! Игрок {winner} выиграл!")
            break

        if is_board_full(board):
            print_board(board)
            print("Игра закончилась ничьей!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


if __name__ == "__main__":
    main()