def average_rating(scores):
	sum=0
	for i in scores:sum+=int(i)
	return(sum/len(scores))

#заполнение словаря
journal=[]

while True:
	ext=input('Класс:')
	if ext=='exit': break
	scoress=input('Оценки: ')
	journal.append({'school_class': ext, 'scores': scoress.split(' ')})
#print (journal)
school_assessments=[]
print('средние оценки:')
for i in journal:

	print('Класс',i['school_class'],' оценка: ',average_rating(i['scores']))
	school_assessments+=i['scores']
print(' оценка по школе: ',average_rating(school_assessments))

