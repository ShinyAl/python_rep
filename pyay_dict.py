	pyg = 'ay'
	
	original = raw_input('Enter a word:')
	
	if len(original) > 0 and original.isalpha():
	#здесь проверяем, что в выражении есть символы и они не содержат числа
	    word = original.lower()
	#здесь меняем в слове все буквы на строчные
	    first = word[0]
	#здесь берем первую букву в слове
	    new_word = word + first + pyg
	#здесь складываем новое слово из исходного + его первой буквы + окончания ay
	    print new_word
	    new_word = new_word[1:len(new_word)]
	#здесь берем у нового слова только то, что лежит между первой и последней буквой
	    print new_word
	else:
	    print 'empty'
