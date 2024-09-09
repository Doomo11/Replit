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
      # print(puzzle)
      # print(i)
      # print()

  print(gaps)
  check = True
  mlength = 10
  for i in gaps.values():
    if len(i) < mlength:
      mlength = len(i)
      print(mlength)
  if mlength >= 2:
    check = False
  print(puzzle)

  for i in empty_squares:
    if len(gaps[i]) == 1:
      puzzle[i] = gaps[i][0]
      gaps.pop(i)

cor = ''
for i in puzzle:
  cor += str(i) + ','

cor = cor[:-1]
print(cor)
print(gaps)

for i in range(len(cor)):
  if i % 18 != 0:
    print(cor[i], end = '')
  else:
    print()
    print(cor[i], end = '')

# with open('score.txt', 'r') as f:
#   score = int(f.read())

# with open('score.txt', 'w') as f:
#   score += 1
#   f.write(str(score))