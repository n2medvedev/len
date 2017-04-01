while True:
	anwser=input('Укажите возраст  ')
	if anwser=='exit': break
	old=int(anwser)
	if old<7:print('Детский сад')
	elif old<18:print('Школьник')
	elif old<23:print('Студент')
	elif old<60:print('Трудящийся')
	elif old<120:print('Пенсионер')
	else: print('Так долго не живут')