import pprint

board = {'top-L':' ', 'top-M':' ', 'top-R':' ', 
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ', 
            'low-L':' ', 'low-M':' ', 'low-R':' '}

players = {'one':0, 'two':0}

def printBoard():
	print(board['top-L'] + '|' + board['top-M'] + '|' +board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' +board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' +board['low-R'])


def printBoardExplanation():
	print("There are two players. One of them uses \'X\' and the other uses \'O\'. The board looks like this: \n")
	print(str(1) + '|' + str(2)  + '|' + str(3))
	print('-+-+-')
	print(str(4) + '|' + str(5)  + '|' + str(6))
	print('-+-+-')
	print(str(7) + '|' + str(8)  + '|' + str(9))
	print("\n")
	print("Enter these numbers to put X/O in the desired square. The game ends when someone has a full column, row or diagonal")
	print("That's it. Have fun!\n")

def move(str):
	if(str == 'one'):
		str_piece = 'X'
	else:
		str_piece = 'O'
	nb = int(input("Enter your input, player " + str + ":"))
	if( nb == 1 and board['top-L'] == ' '):
		board['top-L'] = str_piece
	elif( nb == 2 and board['top-M'] == ' '):
		board['top-M'] = str_piece
	elif( nb == 3 and board['top-R'] == ' '):
		board['top-R'] = str_piece
	elif( nb == 4 and board['mid-L'] == ' '):
		board['mid-L'] = str_piece
	elif( nb == 5 and board['mid-M'] == ' '):
		board['mid-M'] = str_piece
	elif( nb == 6 and board['mid-R'] == ' '):
		board['mid-R'] = str_piece
	elif( nb == 7 and board['low-L'] == ' '):
		board['low-L'] = str_piece
	elif( nb == 8 and board['low-M'] == ' '):
		board['low-M'] = str_piece
	elif( nb == 9 and board['low-R'] == ' '):
		board['low-R'] = str_piece
	else:
		return 0;
	return 1;

def clearTable():
	for k, v in board.items():
		board[k] = ' '

def checkWin(str1):
	val = 'O'
	if(str1 == 'one'):
		val = 'X'
	if(board['top-L'] == board['top-M'] == board['top-R'] == val or 
	   board['mid-L'] == board['mid-M'] == board['mid-R'] == val or
	   board['low-L'] == board['low-M'] == board['low-R'] == val or


	   board['top-L'] == board['mid-L'] == board['low-L'] == val or 
	   board['top-M'] == board['mid-M'] == board['low-M'] == val or
	   board['top-R'] == board['mid-R'] == board['low-R'] == val or


	   board['top-L'] == board['mid-M'] == board['low-R'] == val or
	   board['low-L'] == board['mid-M'] == board['top-R'] == val):
		return True;
	return False;

def tour():
	while(move('one') == 0):
		print("Try again\n")
	printBoard()
	if(checkWin('one')):
		print('PLAYER ONE WON!!\n')
		players['one'] = players['one']+1
		return True;

	while(move('two') == 0):
		print("Try again\n")
	printBoard() 
	if(checkWin('two')):
		print('PLAYER TWO WON!!\n')
		players['two'] = players['two']+1
		return True;
	return False;


def main():
	str = input("Know the rules?\n")
	if(str == 'no'):
		printBoardExplanation()

	str = input("Ready to play tic-tac-toe?\n")
	while(str == 'yes'):
		win = False;
		print("Let's play")
		printBoard()
		
		if(tour()):
			win = True;

		if(not win and tour()):
			win = True;

		if(not win and tour()):
			win = True;
		
		if(not win and tour()):
			win = True;

		if(not win):
			for k, v in board.items():
				if( v == ' '):
					board[k] = 'X'
			if(checkWin('one')):
				print('PLAYER ONE WON!!\n')
				players['one'] = players['one']+1
			else:
				print('Check!\n')

		str = input("Play again?")
		clearTable()

	if(str == 'no'):
		pprint.pprint(players)

if _name_ == '_main_':
	main()
