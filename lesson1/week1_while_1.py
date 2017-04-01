names=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while True:
	a=names.pop()
	if a=="Валера":
		print("Валера нашелся")
		break
print(names)