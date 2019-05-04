import random
import subprocess as sp
from IPython.display import clear_output

class GameBoard(object):
    def __init__(self,row=6,col=7):
        self.row = row
        self.col = col
        self.board_matrix = [ [ 0 for i in range(col) ] for j in range(row)  ]
        self.num_to_sign = { 1 : '+', 2 : '-' }
        self.turn = True
        
    
    def show(self):
        print(self.board_matrix)
    
    def giv_val(self,r,c):
        r = r-1
        c = c-1
        return self.board_matrix[r][c]
    
    def print_board(self):
        row = self.row*4 + 1
        for i in range(row):
            if i %4 == 0 :
                for j in range(self.col):
                    if i == 0:
                        print('+--{}--'.format(j+1),end='')
                    else :
                        print('+-----'.format(j+1),end='')
                print('+')

            else :
                for j in range(self.col):
                    if (i-2)%4 == 0:
                        val = self.board_matrix[int(i/4)][j]
                        print('|  {}  '.format( self.num_to_sign.get( val,' ' ) ),end='')
                    else:
                        print('|     ',end='')
                print('|')
        
    def modify(self,col_num=79):
        
        if self.turn:
            col_list = [ self.board_matrix[i][col_num] for i in range(self.row)  ]
            
            for i in range(len(col_list)-1,-1,-1 )  :
                if col_list[i] == 0 :
                    self.board_matrix[i][col_num] = 1
                    break
        else : 
            
            rand_col_num = random.randint(0,6)
            col_list = [ self.board_matrix[i][rand_col_num] for i in range(self.row)  ]
            
            for i in range(len(col_list)-1,-1,-1 ) :
                if col_list[i] == 0 :
                    self.board_matrix[i][rand_col_num] = 2
                    break
        
        self.turn = not self.turn
    
    def check_validity(self,sign):
    ## check row
        for index,row in enumerate(self.board_matrix):
            if index <= self.col -3:
                for i in range(self.col-3):
                    window = row[i:i+4]
                    if window.count(sign) == 4 :
                        return False

        ## check col
        trasposed = [list(i) for i in zip(*self.board_matrix)]
        for index,col in enumerate(trasposed):
            if index <= self.row -3:
                for i in range(self.row-3):
                    window = col[i:i+4]
                    if window.count(sign) == 4 :
                        return False
        return True
                
a = GameBoard()
count = 0
while True:
    count += 1
#   comment this if on notebook
    tmp = sp.call('cls',shell=True)
#    comment this if on cmd
#    clear_output()
    a.print_board()

    ## start
    
    player_val = input('enter number(1-7): ')
    player_val = int(player_val) - 1 
    # PLAYER TURN
    a.modify(player_val)
    if not a.check_validity(1):
        clear_output()
        a.print_board()
        print('Player won within {} moves'.format(count))
        break
    # COMPUTER TURN
    a.modify()
    if not a.check_validity(2):
        clear_output()
        a.print_board()
        print('Computer won within {} moves'.format(count))
        break