import unittest
from sudoku import SudokuCheck

class TestSudoku(unittest.TestCase):

        def setUp(self):
                self.grid = [[2, 8, 6, 3, 4, 5, 1, 9, 7],
                             [3, 7, 5, 6, 9, 1, 4, 8, 2],
                             [9, 4, 1, 7, 8, 2, 6, 3, 5],
                             [4, 5, 7, 2, 1, 3, 8, 6, 9],
                             [8, 9, 2, 4, 5, 6, 7, 1, 3],
                             [6, 1, 3, 8, 7, 9, 2, 5, 4],
                             [1, 2, 9, 5, 6, 7, 3, 4, 8],
                             [5, 3, 8, 1, 2, 4, 9, 7, 6],
                             [7, 6, 4, 9, 3, 8, 5, 2, 1]]
                self.gridBlank = [[0, 8, 6, 3, 4, 5, 1, 9, 7],
                                  [3, 7, 5, 6, 9, 1, 4, 8, 2],
                                  [9, 4, 1, 7, 8, 2, 6, 3, 5],
                                  [4, 5, 7, 2, 1, 3, 8, 6, 9],
                                  [8, 9, 2, 4, 5, 6, 7, 1, 3],
                                  [6, 1, 3, 8, 7, 9, 2, 5, 4],
                                  [1, 2, 9, 5, 6, 7, 3, 4, 8],
                                  [5, 3, 8, 1, 2, 4, 9, 7, 6],
                                  [7, 6, 4, 9, 3, 8, 5, 2, 1]]
                self.sudoku = SudokuCheck()

        def testLiveCheck(self):
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 1))
                self.assertTrue(self.sudoku.liveCheck(self.gridBlank, 0, 0, 2))
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 3))
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 4))
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 5))
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 6))
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 7))
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 8))
                self.assertFalse(self.sudoku.liveCheck(self.gridBlank, 0, 0, 9))

        def testFinalCheck(self):
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 1
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 2
                self.assertTrue(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 3
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 4
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 5
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 6
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 7
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 8
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))
                self.gridBlank[0][0] = 9
                self.assertFalse(self.sudoku.finalCheck(self.gridBlank))


if __name__ == '__main__':
    unittest.main()
