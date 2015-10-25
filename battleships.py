from random import randint
#make an empty list
board = []

#make a string with OOOOO in cycle
for x in range(5):
	board.append(["O"] * 5)
#place a spaces in string between O
def print_board(board):
	for row in board:
		print " ".join(row)

print "Let's play Battleship!"
print_board(board)
#choose a random row and colon
def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board[0]) - 1)
#make a variable, where we will be store a meaning of this variable
ship_row = random_row(board)
ship_col = random_col(board)

#print ship_row
#print ship_col

#add 4 turns in cycle
for turn in range(4):

#add an input from user with the coordinates
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))

#check inputs with the chosen previously by a program
#if yes, break the cycle
	if guess_row == ship_row and guess_col == ship_col:
  		print "Congratulations! You sunk my battleship!"
  		break
#check if inputs were incorrect
	else:
#check inputs for matching with a play field
   		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
	   			print "Oops, that's not even in the ocean."
#else: you entered the same coordinates as before
   		elif(board[guess_row][guess_col] == "X"):
	   			print "You guessed that one already."
#place X for showing an incorrect coordinate in the field
 		else:
	   			print "You missed my battleship!"
	   			board[guess_row][guess_col] = "X"
#if the coordinates were incorrect for 4 times, print end of game and break
	if turn == 3:
		print "Game Over"
	print "Turn", turn + 1 # Print (turn + 1) here!
	print_board(board)
