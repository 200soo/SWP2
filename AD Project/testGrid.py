import sys
from grid import Grid


grid = Grid()

# 그리드 생성되는 것 확인
grid.createGrid()
print(grid.originGrid)

print('\n')

# 어려움 모드일 때 blank 생성 확인
grid.createBlank(1)
print(grid.blankGrid)

print('\n')

# 쉬움 모드일 때 blank 생성 확인
grid.createBlank(2)
print(grid.blankGrid)
