board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board():
  print("   0  1  2")
  for i, row in enumerate(board):
    print(i, row)

def get_move(player):
  while True:
    col = input(f"{player}, enter column: ")
    row = input(f"{player}, enter row: ")
    if board[int(row)][int(col)] == " ":
      board[int(row)][int(col)] = player
      break
    else:
      print("That space is already occupied. Try again.")

def has_won(player):
  # check rows
  for row in board:
    if row == [player, player, player]:
      return True
  # check columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def main():
  draw_board()
  while True:
    get_move("X")
    draw_board()
    if has_won("X"):
      print("X has won!")
      break
    get_move("O")
    draw_board()
    if has_won("O"):
      print("O has won!")
      break

main()
