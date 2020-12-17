import unittest
import numpy as np
from polar_maze import make_grid

class MakeGridTest(unittest.TestCase):
  def test_check_grid_has_a_single_zero_row(self):
    expected_result = np.array([0])
    actual_result = make_grid(1)
    self.assertEqual(expected_result, actual_result)

  def test_check_grid_has_two_rows(self):
    expected_result = np.array([[0,0],[0,0]])
    actual_result = make_grid(2,2)
    np.testing.assert_array_equal(expected_result, actual_result)

if __name__ == '__main__':
  unittest.main(verbosity = 2)
