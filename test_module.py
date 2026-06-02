import unittest
from sea_level_predictor import draw_plot


class UnitTests(unittest.TestCase):

    def test_plot(self):
        ax = draw_plot()
        self.assertIsNotNone(ax)


if __name__ == "__main__":
    unittest.main()
