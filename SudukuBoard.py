from random import randint,shuffle
import random
board1 =[
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 0, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]]

board2 =[
        [0, 0, 0, 2, 0, 0, 0, 6, 3],
        [3, 0, 0, 0, 0, 5, 4, 0, 1],
        [0, 0, 1, 0, 0, 3, 9, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 5, 3, 8, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 6, 3, 0, 0, 5, 0, 0],
        [5, 0, 3, 7, 0, 0, 0, 0, 8],
        [4, 7, 0, 0, 0, 1, 0, 0, 0]
        ]

board3 =[
        [0, 0, 0, 7, 4, 0, 0, 0, 1],
        [0, 7, 1, 0, 0, 5, 9, 0, 0],
        [5, 0, 9, 0, 0, 0, 0, 0, 8],
        [0, 9, 0, 6, 1, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 8, 2, 0, 3, 0],
        [4, 0, 0, 0, 0, 0, 7, 0, 5],
        [0, 0, 7, 3, 0, 0, 8, 1, 0],
        [8, 0, 0, 0, 7, 4, 0, 0, 0]
        ]
board4 =[
        [0, 0, 3, 0, 4, 2, 0, 9, 0],
        [0, 9, 0, 0, 6, 0, 5, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 7, 0, 0, 2, 8, 5],
        [0, 0, 8, 0, 0, 0, 1, 0, 0],
        [3, 2, 9, 0, 0, 8, 7, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 5, 0, 9, 0, 0, 2, 0],
        [0, 8, 0, 2, 1, 0, 6, 0, 0]
        ]

board5 =[
        [0, 8, 0, 0, 3, 0, 0, 0, 2],
        [7, 0, 0, 0, 5, 0, 9, 0, 0],
        [0, 0, 9, 7, 6, 2, 0, 0, 8],
        [0, 0, 0, 6, 0, 0, 5, 8, 0],
        [0, 5, 0, 0, 0, 0, 0, 4, 0],
        [0, 7, 4, 0, 0, 3, 0, 0, 0],
        [3, 0, 0, 1, 4, 6, 7, 0, 0],
        [0, 0, 7, 0, 9, 0, 0, 0, 3],
        [1, 0, 0, 0, 7, 0, 0, 9, 0]
        ]

board6 =[
        [2, 0, 0, 0, 4, 0, 5, 1, 0],
        [0, 0, 3, 6, 8, 0, 9, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 9, 4, 0, 0, 3, 0, 8],
        [0, 3, 0, 9, 2, 8, 0, 5, 0],
        [1, 0, 8, 0, 0, 3, 4, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 2, 0, 9, 1, 8, 0, 0],
        [0, 6, 1, 0, 3, 0, 0, 0, 5]
        ]

global boardshow
board_1=[board4, board5, board6,board1, board2, board3]

boardshow = random.choice(board_1)



def boardprint(playboard):
    for i in range(len(playboard)):
        if i%3==0:
            print("--------------------------") #row i %3==0 then print
        for j in range(len(playboard)):
            if j%3==0 and j!=0:  #col j %3==0 then print
                print(" | ",end=" ") #end /n
            if j==8: #the last row
                print(playboard[i][j]) #It's printing the last column at j=8 posi(i.e col 8)
            else:
                print(str(playboard[i][j])+" ",end=" ") #print col. before 8 after printing end newline

def emptycheck(playboard):
    for rows in range(len(playboard)):
        for cols in range(len(playboard)):
            if playboard[rows][cols] == 0: #checks if the playboard at this position contains 0 or not
                return (rows,cols) #row and col
    return None

def checker(playboard, n, position):
                                        #check rows to find similar number, if yes then false
    for rows in range(len(playboard)):
        if playboard[position[0]][rows] == n and position[1] != rows:  #we are checking if empty space is equal to the number we checking(rows,0)
            return False
    #check columns to find similar number, if yes then false
    for rows in range(len(playboard)):
        if playboard[rows][position[1]] == n and position[0] != rows:  #we are checking if empty spaces is equal to the number we checking(0,cols)#0 here as count is from 0-8 in case of column
            return False
    #check cubes to find similar number, if yes then false
    box_col = position[1] // 3  #for empty checks tuple will return x,y, here y i.e column will be taken, x axis
    box_row = position[0] // 3  #for empty checks tuple will return x,y here x i,e row will be taken, y axis
    for i in range(box_row*3, box_row*3 + 3):  #traversing through the rows
        for j in range(box_col*3, box_col*3 + 3):  #traversng through the cols
            if playboard[i][j] == n and (i, j) != position:  #to check if its equal to the number and if we are not checking the number we just input
                return False

    return True  #after all checks are unsatisfied means true no number has been found matching both row, col or cube

def solve(playboard):#backtracking algo
    finder = emptycheck(playboard)         #finder stores the value returned by emptycheck function
    if not finder:       #if nothing found in finder, then it means board is full and not empty as emptychecker didn't return any value
        return True
    else:
        row, col = finder  #finder returns the tuple returned by emptychecker into the rows,cols
    for i in range(1,10):
        if checker(playboard, i, (row, col)):    #playboard, i= iterating from 1 to 10, row,col being the value returned from empty checker
            playboard[row][col] = i       #if checker is true, it means it is not equal to row,column or cube then put i into playerboard

            if solve(playboard):       #recursively calling solve to check our newboard
                return True

            playboard[row][col] = 0       #after return false from below, we re-set it to 0 to backtrack it, to try again and again check the forloop

    return False           # if i iterates through whole 9 elementsn and still doesnt satifies
boardprint(boardshow)
solve(boardshow)
boardprint(boardshow)



