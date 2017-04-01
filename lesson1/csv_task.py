import csv

answers = {
	'привет'     :'и тебе привет',
	'как дела'   :'отлично',
	'пока'       :'увидимся'
	}
with open('answ.csv', 'w', encoding='utf-8') as f:
	fields = ['key','answer']
	writer = csv.DictWriter(f, fields, delimiter=';')
	writer.writeheader()
	for key in answers:
		writer.writerow({ 'answer': answers[key],'key': key})
	f.close()

# class C:
# 	def foo(self):
# 		print(self)

# c = C()
# c.foo()