#Make a list containing all of the numbers of the sudoku from the csv file in order
with open('sudoku.txt', 'r') as f:
        s = str(f.read())
        print(s)
        s = s.replace('\n', ',')
        puzzle = s.split(',')

print(puzzle)

for i in range(len(puzzle)):
        puzzle[i] = int(puzzle[i])

print(puzzle)

#Make a blank dictionary for all of the numbers and their possible values
gaps = {}
for i in range(len(puzzle)):
        gaps[i] : []

#check what boxes, rows and columns the square is in and add to the dictionary 'gaps' the possible values of a certain empty space entering the index
def check_square(index):
        numbers = [1,2,3,4,5,6,7,8,9]
        possible = []
        
        check = index
        if check in box1:
                print('in box 1')
                box = box1
        elif check in box2:
                print('in box 2')
                box = box2
        elif check in box3:
                print('in box 3')
                box = box3
        elif check in box4:
                print('in box 4')
                box = box4
        elif check in box5:
                print('in box 5')
                box = box5
        elif check in box6:
                print('in box 6')
                box = box6
        elif check in box7:
                print('in box 7')
                box = box7
        elif check in box8:
                print('in box 8')
                box = box8
        elif check in box9:
                print('in box 9')
                box = box9

        
        if check in row1:
                print('in row 1')
                row = row1
        elif check in row2:
                print('in row 2')
                row = row2
        elif check in row3:
                print('in row 3')
                row = row3
        elif check in row4:
                print('in row 4')
                row = row4
        elif check in row5:
                print('in row 5')
                row = row5
        elif check in row6:
                print('in row 6')
                row = row6
        elif check in row7:
                print('in row 7')
                row = row7
        elif check in row8:
                print('in row 8')
                row = row8
        elif check in row9:
                print('in row 9')
                row = row9
        

        if check in column1:
                print('in column 1')
                column = column1
        elif check in column2:
                print('in column 2')
                column = column2
        elif check in column3:
                print('in column 3')
                column = column3
        elif check in column4:
                print('in column 4')
                column = column4
        elif check in column5:
                print('in column 5')
                column = column5
        elif check in column6:
                print('in column 6')
                column = column6
        elif check in column7:
                print('in column 7')
                column = column7
        elif check in column8:
                print('in column 8')
                column = column8
        elif check in column9:
                print('in column 9')
                column = column9

        # print('box:')
        # print(box)
        # print('row:')
        # print(row)
        # print('column')
        # print(column)

        for i in numbers:
                fine = True
                for j in box:
                        if i == puzzle[j]:
                                fine = False
                for j in row:
                        if i == puzzle[j]:
                                fine = False
                for j in column:
                        if i == puzzle[j]:
                                fine = False
                if fine == True:
                        possible.append(i)
        #print(possible)
        gaps[index] = possible
        #print(gaps)
        

        



box1 = [0,1,2,
        9,10,11,
        18,19,20]
box2 =         [3,4,5,
                12,13,14,
                21,22,23]
box3 =                 [6,7,8,
                        15,16,17,
                        24,25,26]
box4 = [27,28,29,
        36,37,38,
        45,46,47]
box5 =         [30,31,32,
                39,40,41,
                48,49,50]
box6 =                  [33,34,35,
                        42,43,44,
                        51,52,53]
box7 = [54,55,56,
        63,64,65,
        72,73,74]
box8 =         [57,58,59,
                66,67,68,
                75,76,77]
box9 =                 [60,61,62,
                        69,70,71,
                        78,79,80]


row1 = [0,1,2,3,4,5,6,7,8]
row2 = [9,10,11,12,13,14,15,16,17]
row3 = [18,19,20,21,22,23,24,25,26]
row4 = [27,28,29,30,31,32,33,34,35]
row5 = [36,37,38,39,40,41,42,43,44]
row6 = [45,46,47,48,49,50,51,52,53]
row7 = [54,55,56,57,58,59,60,61,62]
row8 = [63,64,65,66,67,68,69,70,71]
row9 = [72,73,74,75,76,77,78,79,80]

column1 = [0,9,18,27,36,45,54,63,72]
column2 = [1,10,19,28,37,46,55,64,73]
column3 = [2,11,20,29,38,47,56,65,74]
column4 = [3,12,21,30,39,48,57,66,75]
column5 = [4,13,22,31,40,49,58,67,76]
column6 = [5,14,23,32,41,50,59,68,77]
column7 = [6,15,24,33,42,51,60,69,78]
column8 = [7,16,25,34,43,52,61,70,79]
column9 = [8,17,26,35,44,53,62,71,80]















# box1 = [[0],[1],[2],
#         [9],[10],[11],
#         [18],[19],[20]]
# box2 = [[3],[4],[5],
#         [12],[13],[14],
#         [21],[22],[23]]
# box3 = [[6],[7],[8],
#         [15],[16],[17],
#         [24],[25],[26]]
# box4 = [[27],[28],[29],
#         [36],[37],[38],
#         [45],[46],[47]]
# box5 = [[30],[31],[32],
#         [39],[40],[41],
#         [48],[49],[50]]
# box6 = [[33],[34],[35],
#         [42],[43],[44],
#         [51],[52],[53]]
# box7 = [[54],[55],[56],
#         [63],[64],[65],
#         [72],[73],[74]]
# box8 = [[57],[58],[59],
#         [66],[67],[68],
#         [75],[76],[77]]
# box9 = [[60],[61],[62],
#         [69],[70],[71],
#         [78],[79],[80]]


# row1 = [[0],[1],[2],[3],[4],[5],[6],[7],[8]]
# row2 = [[9],[10],[11],[12],[13],[14],[15],[16],[17]]
# row3 = [[18],[19],[20],[21],[22],[23],[24],[25],[26]]
# row4 = [[27],[28],[29],[30],[31],[32],[33],[34],[35]]
# row5 = [[36],[37],[38],[39],[40],[41],[42],[43],[44]]
# row6 = [[45],[46],[47],[48],[49],[50],[51],[52],[53]]
# row7 = [[54],[55],[56],[57],[58],[59],[60],[61],[62]]
# row8 = [[63],[64],[65],[66],[67],[68],[69],[70],[71]]
# row9 = [[72],[73],[74],[75],[76],[77],[78],[79],[80]]

# column1 = [[0],[9],[18],[27],[36],[45],[54],[63],[72]]
# column2 = [[1],[10],[19],[28],[37],[46],[55],[64],[73]]
# column3 = [[2],[11],[20],[29],[38],[47],[56],[65],[74]]
# column4 = [[3],[12],[21],[30],[39],[48],[57],[66],[75]]
# column5 = [[4],[13],[22],[31],[40],[49],[58],[67],[76]]
# column6 = [[5],[14],[23],[32],[41],[50],[59],[68],[77]]
# column7 = [[6],[15],[24],[33],[42],[51],[60],[69],[78]]
# column8 = [[7],[16],[25],[34],[43],[52],[61],[70],[79]]
# column9 = [[8],[17],[26],[35],[44],[53],[62],[71],[80]]