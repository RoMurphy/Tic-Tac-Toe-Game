theBoard = {'top-L': '-', 'top-M': '-', 'top-R': '-', 'mid-L': '-', 'mid-M': '-', 'mid-R': '-', 'btm-L': '-', 'btm-M': '-', 'btm-R': '-'}
print("Welcome to Tic Tac Toe or x's and o's:\nYou go first!")
      
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['btm-L'] + '|' + board['btm-M'] + '|' + board['btm-R'])
print("The board")
printBoard(theBoard)
print("Do you choose:\ntop-L, top-M, top-R?\nmid-L, mid-M, mid-R?\nbtm-L, btm-M, btm-R?")
first_move = input()
if first_move == 'top-L':
        theBoard['top-L'] = 'x'
elif first_move == 'top-M':
        theBoard['top-M'] = 'x'
elif first_move == 'top-R':
        theBoard['top-R'] = 'x'
elif first_move == 'mid-L':
        theBoard['mid-L'] = 'x'
elif first_move == 'mid-M':
        theBoard['mid-M'] = 'x'
elif first_move == 'mid-R':
        theBoard['mid-R'] = 'x'
elif first_move == 'btm-L':
        theBoard['btm-L'] = 'x'
elif first_move == 'btm-M':
        theBoard['btm-M'] = 'x'
elif first_move == 'btm-R':
        theBoard['btm-R'] = 'x'
else:
        print('Please check your spelling!\nInput is case sensitive and must match options given')
        print("Do you choose:\ntop-L, top-M, top-R?\nmid-L, mid-M, mid-R?\nbtm-L, btm-M, btm-R?")
printBoard(theBoard)

