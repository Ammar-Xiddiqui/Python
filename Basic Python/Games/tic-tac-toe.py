#  tic-tac-toe
x=[]
z=1
for i in range(3):
    y=[]
    for j in range(3):
        y.append(z)
        z+=1
    x.append(y)
def draw_board(board):
      for i in range(3):
          for j in range(3):
              print(board[i][j], end=' ')
          print()
# draw_board(x)
def make_right_a(board):
    k=1
    while k<2:
        n=int(input('first player (select number from the board and enter it ): '))
        n=n-1
        j=n%3
        i=n//3
        if n<9 and board[i][j]!='a'and board[i][j]!='b':
            board[i][j]='a'
            k+=1
    if board[i][0] == board[i][1] == board[i][2]:
        return True
    elif board[0][j] == board[1][j] == board[2][j]:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'a':
        return True
    elif board[0][2] == board[1][1] == board[2][0] == 'a':
        return True
    else:
        return False
draw_board(x)

def make_right_b(board):
    k=1
    while k<2:
        n=int(input('second player (select number from the board and enter it ): '))
        n=n-1
        i=n//3
        j=n%3
        if n<9 and board[i][j]!='a' and board[i][j]!='b':
            board[i][j]='b'
            k+=1
    if board[i][0] == board[i][1] == board[i][2]:
        return True
    elif board[0][j] == board[1][j] == board[2][j]:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'b':
        return True
    elif board[0][2] == board[1][1] == board[2][0] == 'b':
        return True
    else:
        return False
num=1
for l in range(9):
    if l%2==0:
        if make_right_a(x) == False:
            draw_board(x)
        else:print('winner is A');draw_board(x);break
    elif l % 2 == 1:
        if make_right_b(x) == False:
            draw_board(x)
        else:
            print('winner is b');draw_board(x);break
    if l==8:print('game is draw')

