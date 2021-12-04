import sys
from grid import Grid
from sudoku import SudokuCheck

grid = Grid()
sudoku = SudokuCheck()

# 그리드 생성되는 것 확인
grid.createGrid()
for row in range(0, 9):
    res = ''
    for col in range(0, 9):
        res += str(grid.originGrid[row][col]) + ' '
    print(res)
print('\n')

# 어려움 모드일 때 blank 생성 확인
print('difficult')
grid.createBlank(1)
for row in range(0, 9):
    res = ''
    for col in range(0, 9):
        res += str(grid.blankGrid[row][col]) + ' '
    print(res)
print('\n')

# 쉬움 모드일 때 blank 생성 확인
print('easy')
grid.createBlank(2)
for row in range(0, 9):
    res = ''
    for col in range(0, 9):
        res += str(grid.blankGrid[row][col]) + ' '
    print(res)
print('\n')

print(sudoku.finalCheck(grid.originGrid))
print(sudoku.finalCheck(grid.blankGrid))
