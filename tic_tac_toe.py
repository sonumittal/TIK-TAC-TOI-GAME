import random
import sys
board=[0,1,2,
       3,4,5,
       6,7,8]
def show():
     print(board[0],'|',board[1],'|',board[2])
     print("---------")
     print(board[3],'|',board[4],'|',board[5])
     print("---------")
     print(board[6],'|',board[7],'|',board[8])
show()

#--check true functions- step 2 for understand simply-
def checkLine(char,spot1,spot2,spot3):
     if board[spot1]==char and board[spot2]==char and board[spot3]==char:
          return True
def checkAll(char):
     if checkLine(char,0,1,2):
          return True
     if checkLine(char,3,4,5):
          return True
     if checkLine(char,6,7,8):
          return True
     if checkLine(char,0,3,6):
          return True
     if checkLine(char,1,4,7):
          return True
     if checkLine(char,2,5,8):
          return True
     if checkLine(char,0,4,8):
          return True
     if checkLine(char,2,4,6):
          return True
#--------------

while True: #--step 1-
     user_input=int(input("Select a spot: "))
     if board[user_input]!='x' and board[user_input]!='o':
          board[user_input]='x'

          #--check and declar result---
          if  checkAll('x')==True:
               show()
               print("---X WINS----")
               sys.exit()
               break
             #----------
          while True:
               random.seed() #--give a random generator
               opponent=random.randint(0,8) #--take only 1 to 8 integer

               if board[opponent]!='o' and board[opponent]!='x':
                    board[opponent]='o'

                    #--check and declar---
                    if  checkAll('o')==True:
                         show()
                         print("---O WINS----")
                         sys.exit()
                         break
                    #--------
                    break;
     else:
          print('Try Again, This spot is taken')
     show()
          
