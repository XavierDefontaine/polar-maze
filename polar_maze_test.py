import unittest
from unittest import mock
from unittest.mock import patch
import numpy as np
from polar_maze import make_grid
from polar_maze import initialise_player
from polar_maze import move_player

class MakeGridTest(unittest.TestCase):
  def test_check_grid_has_a_single_zero_row(self):
    expected_result = np.array([0])
    actual_result = make_grid(1)
    self.assertEqual(expected_result, actual_result)

  def test_check_grid_has_two_rows(self):
    expected_result = np.array([[0,0],[0,0]])
    actual_result = make_grid(2,2)
    np.testing.assert_array_equal(expected_result, actual_result)

class InitialisePlayerTest(unittest.TestCase):
  def test_player_starts_in_top_left_and_is_represented_by_1(self):
    grid = np.array([
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
    ])
    expected_result = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    actual_result = initialise_player(grid)
    np.testing.assert_array_equal(expected_result, actual_result)

class MovePlayerTest(unittest.TestCase):
  def test_player_starts_in_top_left_and_moves_right(self):
    grid = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    expected_result = np.array([
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    actual_result = move_player(grid, 'R')
    np.testing.assert_array_equal(expected_result, actual_result)

    

if __name__ == '__main__':
  unittest.main(verbosity = 2)
