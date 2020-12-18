import numpy as np

class Game():
  def __init__(self):
    grid_dimentions = self.get_grid_dimensions()
    self.grid = self.make_grid(grid_dimentions[0], grid_dimentions[1])
    self.initialise_player_location()
    self.initialise_finish_line()

  def get_grid_dimensions(self):
    grid_shape = input("Do you want a square or rectangle?")
    if grid_shape == "square":
      grid_size = input("What size of square?")
      return (int(grid_size), None)
    elif grid_shape == "rectangle":
      grid_rows = input("How many rows in the rectangle?")
      grid_columns = input("How many columns in the rectangle?")
      return (
        int(grid_rows),
        int(grid_columns),
      )
    else:
      return self.get_grid_dimensions()

  def make_grid(self, row, column = None):
    if column == None:
      column = row
    return np.zeros((row, column), dtype = int)

  def initialise_player_location(self):
    self.grid[0,0] = 1

  def move_player(self, direction):
    previous_player_location = (np.where(self.grid == 1))
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
    self.grid[previous_player_location] = 0

    if self.grid[new_player_location] == 2:
      print("You won")
      return
    else:
      self.grid[new_player_location] = 1

  def initialise_finish_line(self, row = -1, column = -1):
    self.grid[row, column] = 2

  def get_player_move_choice(self):
    player_choice = input("What direction do you want to move?\nType U D L or R\n")
    return player_choice
"""METHOD get player move choice
ASK player what direction to move
RECEIVE input
RETURN input
"""

"""METHOD make move
CALL get player move choice
CALL move player
"""

"""METHOD render game on screen
START loop
  PRINT grid
  CALL make move
  BREAK if player reaches finish line
"""







"""IF name == main
START loop
  CALL render game on screen
"""
