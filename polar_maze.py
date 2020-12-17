import numpy as np

def make_grid(row, column = None):
  if column == None:
    column = row
  return np.zeros((row, column), dtype = int)

def initialise_player(grid):
  grid[0,0] = 1
  return grid
