
#Задание

 #   Напечатайте в консоль даты: вчера, сегодня, месяц назад
 #   Превратите строку "01/01/17 12:10:03.234567" в объект datetime
from datetime import datetime, date, timedelta
import calendar
import locale

#if __name__ == "__main__"  - дает ошибку
def main():
    date_now = date.today()
    days_manth = -1*calendar.monthrange(date_now.year,date_now.month-1)[1]+1
    print(days_manth)
    d_m = [days_manth,'месяц назад ']
    dif=[[-1,'вчера'],[0,'сегодня'],[1,'завтра'],d_m]
    
    
    for d_t in dif:
        delta = timedelta(days=d_t[0])
        dt = date_now+delta
        d_time = dt.strftime('%A %d %B %Y')
        print (d_t[1],d_time)
    print ('\n Превращаем строку "01/01/17 12:10:03.234567" в объект datetime :')
    date_str="01/01/17 12:10:03.234567"
    dt = datetime.strptime(date_str, '%m/%d/%y %H:%M:%S.%f')
    print(dt)

#locale.setlocale(locale.LC_TIME, "ru_RU") - дает ошибку
main()

