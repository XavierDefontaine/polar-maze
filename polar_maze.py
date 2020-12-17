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
  
  if direction == 'R':
    grid[player_location] = 0
    grid[
      player_location[0],
      player_location[1] + 1,
    ] = 1
  return grid
