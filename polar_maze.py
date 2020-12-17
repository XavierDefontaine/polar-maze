import numpy as np

class Game():

  def __init__(self):
    pass

  def make_grid(self, row, column = None):
    if column == None:
      column = row
    return np.zeros((row, column), dtype = int)

  def initialise_player_location(self, grid):
    grid[0,0] = 1
    return grid

  def move_player(self, grid, direction):
    previous_player_location = (np.where(grid == 1))
    if direction == 'R':
      new_player_location = [
        previous_player_location[0],
        previous_player_location[1] + 1,
      ]
    elif direction == 'D':
      new_player_location = [
        previous_player_location[0] + 1,
        previous_player_location[1],
      ]
    elif direction == 'U':
      new_player_location = [
        previous_player_location[0] - 1,
        previous_player_location[1],
      ]
    elif direction == 'L':
      new_player_location = [
        previous_player_location[0],
        previous_player_location[1] - 1,
      ]
    grid[previous_player_location] = 0

    if grid[new_player_location] == 2:
      print("You won")
      return
    else:
      grid[new_player_location] = 1

    return grid

  def initialise_finish_line(self, grid, row = -1, column = -1):
    grid[row, column] = 2
    return grid



# def play_game(self):
#   start_game()
#   > loop
#   print("Enter your next move (L,R,U,D)")
#   move = input()
#   new_grid = move_player(grid, move)
#   print(new_grid)
#   # break when winning

# def start_game(self):
#   print("Enter the number of rows and columns")
#   row= input(), column=input()
#   grid = make_grid(row,column)
#   initialise_player
#   initialise_finish_line
#   print(grid)