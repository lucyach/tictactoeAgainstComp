# Initiation
from processing import*
import random
import time
thewinner = ""

print "You are O. The computer is X."
board = ["_0", "_1", "_2", "_3", "_4", "_5", "_6", "_7", "_8"]

#FirstMoves
def printBoard():
  print ""
  print board[0: 3]
  print board[3: 6]
  print board[6: 9]
  
def chosen():
  choice=input("Which spot would you like to select?")
  if board[int(choice)] == "O" or board[int(choice)] == "X":
    print "You can't play there, that space is taken. Please choose someplace else."
    chosen()
  else:
    board[int(choice)] = "O"

def randomCom():
  com_choice = random.randint(0, 8)
  if board[com_choice] == "O" or board[com_choice] == "X":
    randomCom()
  else:
    board[com_choice] = "X"

def winCheck(x,y,z):
  if board[x] == "X" and board[z] == "X" and board[y] == "_" + str(y):
    board[y] = "X"
    return True
  if board[y] == "X":
    if board[x] == "X" and board[z] == "_" + str(z):
      board[z] = "X"
      return True
    if board[z] == "X" and board[x] == "_" + str(x):
      board[x] = "X"
      return True
  else:
    return False

def lineCheck(x, y, z):
  if board[x] == "O" and board[z] == "O" and board[y] == "_" + str(y):
    board[y] = "X"
    return True
  if board[y] == "O":
    if board[x] == "O" and board[z] == "_" + str(z):
      board[z] = "X"
      return True
    if board[z] == "O" and board[x] == "_" + str(x):
      board[x] = "X"
      return True
  else:
    return False

def computerTurn():
    if winCheck(0, 1, 2):
      return
    elif winCheck(3, 4, 5):
     return
    elif winCheck(6, 7, 8):
      return
    elif winCheck(0, 3, 6):
      return
    elif winCheck(1, 4, 7):
      return
    elif winCheck(2, 5, 8):
      return
    elif winCheck(0, 4 ,8):
      return
    elif winCheck(2, 4, 6):
      return
    elif board[4] == "_4":
      board[4] = "X"
      return
    else:
      if lineCheck(0, 1, 2):
        return
      elif lineCheck(3, 4, 5):
        return
      elif lineCheck(6, 7, 8):
        return
      elif lineCheck(0, 3, 6):
        return
      elif lineCheck(1, 4, 7):
        return
      elif lineCheck(2, 5, 8):
        return
      elif lineCheck(0, 4 ,8):
        return
      elif lineCheck(2, 4, 6):
        return
      else:
        randomCom()

def areTheyEqual():
  global thewinner
  if not board[0] == "_0" and not board[1] == "_1" and not board[2] == "_2" and not board[3] == "_3" and not board[4] == "_4" and not board[5] == "_5" and not board[6] == "_6" and not board[7] == "_7" and not board[8] == "_8":
    print "Cat's Game!"
    thewinner = "Both you and the computer"
    return True
  if board[0]==board[3]==board[6]:
    if board[0] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True
  if board[1]==board[4]==board[7]:
    if board[1] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True
  if board[2]==board[5]==board[8]:
    if board[2] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True
  if board[0]==board[1]==board[2]:
    if board[0] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True
  if board[0]==board[4]==board[8]:
    if board[0] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True
  if board[3]==board[4]==board[5]:
    if board[3] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True
  if board[6]==board[7]==board[8]:
    if board[6] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True
  if board[2]==board[4]==board[6]:
    if board[2] == "X":
      thewinner = "The Computer"
    else:
      thewinner = "You"
    return True

while not areTheyEqual():
  printBoard()
  chosen()
  areTheyEqual()
  printBoard()
  computerTurn()
  areTheyEqual()

printBoard()
print "END OF GAME."
print "The win goes to "+ thewinner + "!"