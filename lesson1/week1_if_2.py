def string_comparison(st1,st2='learn'):
	if st1==st2: return(1)
	if st2=='learn': return(3)
	if len(st1)>len(st2): return(2)
	return 4


while True:
	anwser1=input('Введите строку1  ')
	anwser2=input('Введите строку2  ')
	res=string_comparison(anwser1,anwser2)
	print(res)
	if res==4: break
	