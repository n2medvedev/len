
#Задание

 #   Напечатайте в консоль даты: вчера, сегодня, месяц назад
 #   Превратите строку "01/01/17 12:10:03.234567" в объект datetime
from datetime import datetime, date, timedelta
import calendar
import locale

def main():
    date_now = date.today()
    
    dif=[
    	[-1,'вчера'],
    	[0,'сегодня'],
    	[1,'завтра'],
    	[-calendar.monthrange(date_now.year,date_now.month-1)[1],'месяц назад ']
    	]
    
    
    for d_days,d_text in dif:
        delta = timedelta(days=d_days)
        dt = date_now+delta
        d_time = dt.strftime('%A %d %B %Y')
        print (d_text,d_time)
    print ('\n Превращаем строку "01/01/17 12:10:03.234567" в объект datetime :')
    date_str="01/01/17 12:10:03.234567"
    dt = datetime.strptime(date_str, '%m/%d/%y %H:%M:%S.%f')
    print(dt)

locale.setlocale(locale.LC_TIME, "ru_RU.utf-8") # дает ошибку
if __name__ == "__main__" :
	main()

