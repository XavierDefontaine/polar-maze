import numpy as np

class Game():

  def __init__(self):
    # self.grid = actually_construct_grid()  
    # grid = make_grid(row,column)
    # initialise_player
    # initialise_finish_line
    # print(grid)

    # METHOD get grid dimentions
    #   ASK the player if they want a square or rectangle
    #   IF 'square'
    #   THEN ask for the size of the square 
    #     RETURN a tuple of (number entered, number entered)
    #   ELSE
    #     ASK for height
    #     ASK for length
    #     RETURN a tuple of (height, length)

    """
    METHOD actually construct grid
      CALL get grid dimentions
        grid_dimentions = tuple of (x, y) OR (x, x)
      CALL make grid
        USE grid_dimentions
      # CALL init player location
      # CALL init finish
      RETURN grid

    """

  # def play_game(self):
  #   start_game()
  #   > loop
  #   print("Enter your next move (L,R,U,D)")
  #   move = input()
  #   new_grid = move_player(grid, move)
  #   print(new_grid)
  #   # break when winning

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

