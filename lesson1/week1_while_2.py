def find_person(name):
	names=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
	for i in names:
		if i==name: return(name+' нашелся')
	return(name+' не числится')

print(find_person('Валера'))
print(find_person('Петя'))
print(find_person('Iren'))