from operator import mul
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

#OPERATORS = {'*': mul}
#OPERATORS['*'](1, 2)

def calulator(bot,update,pure_str):
    bot.sendMessage(update.message.chat_id, "вычисляю... ")

    #удалить все пробелы
    operation='+-*/'
    operands = ['']
    list_operators=[]
    num_operands = 0
    for i in pure_str:
        if i != ' ':
            if i in operation:
                list_operators.append(i)
                num_operands += 1
                operands.append('')
            else:
                operands[num_operands] += i
    result = 
    
    try:
        
        num=[float(a[0]),float(a[2])]
    except:
        bot.sendMessage(update.message.chat_id, "операторы в выражении - не  числа ")
    else:
        b=0
        print(a[1],)
        if a[1] == '+': 
            b=num[0] + num[1]
        elif a[1] == '-':
            b=num[0] - num[1]
        elif a[1] == '*' : 
            b=num[0] * num[1]
        elif a[1] == '/' : 
            b=num[0] / num[1]
        print(b)

        bot.sendMessage(update.message.chat_id, "ответ "+str(b))




def talk_to_me(bot, update):
    pure_str=update.message.text.strip()
    bot.sendMessage(update.message.chat_id, "получил "+pure_str)
    if pure_str[-1] == '=':
        calulator(bot,update,pure_str[:-1])


def show_error(bot, update, error):
    print(error)

#обработка команды старт
def greet_user(bot, update):
    print(bot)
    print(update)
    print('вызван Старт')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

#Подсчет количества слов
def word_count(bot, update):
    print ('wordcount - RUN')
    print('Update=',update)
    print('BOT=',bot)
    #for idi in update:
    print(update.message.text)
    bot.sendMessage(update.message.chat_id,text='Сейчас посчитаем....')
    word_str = update.message.text.partition('/wordcount')
    pure_str = word_str[2].strip()
    print(pure_str)
    first_sim = pure_str[0]
    last_sim =  pure_str[-1]
    if not(first_sim == last_sim and (first_sim=='"')):
        bot.sendMessage(update.message.chat_id,text='УПСССС,  не строка (((')
    else: 

        list_of_word = pure_str[1:-1].split(' ')
        print(list_of_word)
        i = 0
        #удаляем пробелы между словами
        while i < len(list_of_word):
            if list_of_word[i] == '':
                list_of_word.pop(i)
            else:
                i += 1
        print(list_of_word,'\n count_=',len(list_of_word))
        bot.sendMessage(update.message.chat_id,text='вы ввели ' + str(len(list_of_word)) + ' слов')

 



def main():
    updater = Updater("350203777:AAFM5aYBNc2WpHlt-t8VZMCS0Wz49MjokAA")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('wordcount', word_count))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

main()