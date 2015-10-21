	from random import randint
	#создаем пустой список
	board = []
	
	#в цикле заполняем строчки 5ю буквами О (море типа)
	for x in range(5):
	    board.append(["O"] * 5)
	#расставляем пробелы между строчками
	def print_board(board):
	    for row in board:
	        print " ".join(row)
	
	print "Let's play Battleship!"
	print_board(board)
	#рандомом выбираем значения строки и столбца для корабля
	def random_row(board):
	    return randint(0, len(board) - 1)
	
	def random_col(board):
	    return randint(0, len(board[0]) - 1)
	#создаем переменную, где храним значения положения корабля
	ship_row = random_row(board)
	ship_col = random_col(board)
	
	#здесь выводим значения положения корабля для теста
	#print ship_row
	#print ship_col
	
	#добавляем 4 подхода в цикле, не забываем про отступы
	for turn in range(4):
	    
	    #добавляем ручной ввод значения корабля
	    guess_row = int(raw_input("Guess Row:"))
	    guess_col = int(raw_input("Guess Col:"))
	
	#проверяем на соответствует ли введенные значения выбранным
	#если да, выходим из цикла
	    if guess_row == ship_row and guess_col == ship_col:
	       print "Congratulations! You sunk my battleship!"
	       break
	#здесь проверяем условия, когда значения введены некорректные
	    else:
	#проверяем соответсвуют ли значения сетке игрового поля
	       if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
	           print "Oops, that's not even in the ocean."
	#в ином случае если повторно введены теже значения
	       elif(board[guess_row][guess_col] == "X"):
	           print "You guessed that one already."
	#отмечаем на поле некорректно введенные значения Х
	       else:
	           print "You missed my battleship!"
	           board[guess_row][guess_col] = "X"
	#если 4 раза координаты корабля не угаданы. пишем о конце игры
	    if turn == 3:
	            print "Game Over"
	    print "Turn", turn + 1 # Print (turn + 1) here!
	print_board(board)
