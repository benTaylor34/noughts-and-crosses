board = [['.' for _ in range(3)] for _ in range(3)]
print("", board[0],"\n", board[1], "\n", board[2])

game=True
i=0
try:
    while game:
        # get move
        if i%2:
            while True:    
                #player 2s turn
                move = input("P2(O) please input your grid move (x,y):").replace(" ","")
                try:
                    y, x = map(int, move.split(','))#y=row, x=col
                    y-=1
                    x-=1
                    if -1<x<3 and -1<y<3 and board[y][x] == '.':
                        board[y][x] = 'O'
                        break
                except ValueError:
                    print('please enter a valid move or quit (crtl+c)')

        else:
            while True:    
                #player 1s turn
                move = input("P1(X) please input your grid move (x,y):").replace(" ","")
                try:
                    y, x = map(int, move.split(','))
                    y-=1
                    x-=1
                    if -1<x<3 and -1<y<3 and board[y][x] == '.':
                        board[y][x] = 'X'
                        break
                except ValueError:
                    print('please enter a valid move or quit (crtl+c)')

        #dipslay board
        print("", board[0],"\n", board[1], "\n", board[2])
        #check the board
        for row in board:
            if row[0] == row[1] == row[2] !='.':
                print(f"winner is {row[0]}")
                game=False
                break

        for c in range(3):
            if board[0][c]==board[1][c]==board[2][c]!='.':
                print(f"winner is {board[0][c]}")
                game=False
                break
        
        if board[0][0] == board[1][1] == board[2][2] != '.':
            print(f'winner is {board[0][0]}')
            game=False

        if board[0][2] == board[1][1] == board[2][0] != '.':
            print(f'winner is {board[0][2]}')
            game=False

        i+=1
        if i>=9:
            print("Draw :/")
            game=False

except KeyboardInterrupt:
    pass