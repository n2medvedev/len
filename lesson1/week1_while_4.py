def get_answer(frase):
    answer = {'привет':'И тебе привет','как дела':'Отлично','пока':'Увидимся'}
    frase = frase.lower()
    try:
        return answer[frase]
    except KeyError:
        return 'Извини,плохая связь'

def ask_user(correct_answer='хорошо',аnswer_to_exit='Увидимся'):
    answer = ' Поболтаем?\n                                         '   
     
    while answer != аnswer_to_exit: 
        try:
            answer = get_answer(input(answer + '\n'+' '*20))
        except KeyboardInterrupt :
            answer = аnswer_to_exit
        except :          #  пришлось вставить ,  вылетала из-за кодировки   
            print(answer)
    
    print(аnswer_to_exit)
    
    
def main():
    ask_user()
main()

