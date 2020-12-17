import unittest
import numpy as np
from polar_maze import make_grid

class MakeGridTest(unittest.TestCase):
  def test_make_grid_returns_numpy_array(self):
    expected_type = np.array
    actual_type = make_grid()
    self.assertEqual(actual_type, expected_type)

if __name__ == '__main__':
  unittest.main(verbosity = 2)
