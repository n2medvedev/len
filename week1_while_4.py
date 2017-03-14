def get_answer(a):
	answer={'привет':"И тебе привет","как дела":"Отлично","пока":"Увидимся"}
	a=a.lower()
	if a in answer:return(answer[a])
	return("Извини,плохая связь")

def ask_user(correct_answer="хорошо",аnswer_to_exit="Увидимся"):
	answer=' Поболтаем?'
	while answer!=аnswer_to_exit: 
		answer=get_answer(input(answer+' '))
	print(answer)	
def main():
	ask_user()
main()

