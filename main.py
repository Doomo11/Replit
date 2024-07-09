# My sudoku solver

from setup import *

### ### ###
#1# #2# #3#
### ### ###
### ### ###
#4# #5# #6#
### ### ###
### ### ###
#7# #8# #9#
### ### ###

possible = [1,2,3,4,5,6,7,8,9]


check = True
while check:
  #make a list of all of the empty squares
  empty_squares = [i for i in range(len(puzzle)) if puzzle[i] == 0 ]
  print('Empty squares:')
  print(empty_squares)
  
  for i in empty_squares:
    check_square(i)
    if len(gaps[i]) == 1:
      puzzle[i] = gaps[i][0]
      gaps.pop(i)
      # print(puzzle)
      # print(i)
      # print()

  print(gaps)
  check = False
  for i in gaps.values():
    if len(i) > 1:
      check = True
  print(puzzle)

cor = ''
for i in puzzle:
  cor += str(i) + ','

cor = cor[:-1]
print(cor)

with open('score.txt', 'r') as f:
  score = int(f.read())

with open('score.txt', 'w') as f:
  score += 1
  f.write(str(score))