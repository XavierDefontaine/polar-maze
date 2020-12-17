import numpy as np

def make_grid(row, column = None):
  if column == None:
    column = row
  return np.zeros((row, column), dtype = int)

def initialise_player(grid):
  grid[0,0] = 1
  return grid

def move_player(grid, direction):
  player_location = (np.where(grid == 1))
  grid[player_location] = 0

  if direction == 'R':
    grid[
      player_location[0],
      player_location[1] + 1,
    ] = 1
  elif direction == 'D':
    grid[
      player_location[0] + 1,
      player_location[1],
    ] = 1
  elif direction == 'U':
    grid[
      player_location[0] - 1,
      player_location[1],
    ] = 1
  elif direction == 'L':
    grid[
      player_location[0],
      player_location[1] - 1,
    ] = 1
  return grid

def initialise_finish_line(grid, row = -1, column = -1):
  grid[row, column] = 2
  return grid
