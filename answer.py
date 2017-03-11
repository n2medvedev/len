def get_answer(a):
	answer={'привет':"И тебе привет","как дела":"Отлично","пока":"Увидимся"}
	a=a.lower()
	if a in answer:return(answer[a])
	return("Извини,плохая связь")
while True:
	c=input("Прием:")
	g=get_answer(c)
	print(g)
	if g=="Извини,плохая связь":
		break
	

	