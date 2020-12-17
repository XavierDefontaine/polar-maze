import numpy as np

def make_grid(row, column = None):
  if column == None:
    column = row
  return np.zeros((row, column), dtype = int)

def initialise_player(grid):
  grid[0,0] = 1
  return grid

def move_player(grid, direction):
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
  grid[new_player_location] = 1
  return grid

def initialise_finish_line(grid, row = -1, column = -1):
  grid[row, column] = 2
  return grid
