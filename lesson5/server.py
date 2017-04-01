from flask import Flask,abort,request
from datetime import datetime
from news_list import all_news

from req import get_weather


city_id = 524901
apikey = '7625ce8a3c25d35969acfa3957fb8fc9'

app = Flask(__name__)

@app.route('/')  # определяем страницу 

def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=metric' % (city_id, apikey)
    cur_date = datetime.now().strftime('%d,%m,%Y')
 
    weather = get_weather(url)

    result = '<p><b>температура : </b> %s </p>' % weather['main']['temp']
    result += '<p><b>температура min : </b> %s </p>' % weather['main']['temp_min']
    result += '<p><b>температура max: </b> %s </p>' % weather['main']['temp_max']
    result += '<p><b>Город : </b> %s </p>' % weather['name']
    result += '<p><b>Дата: </b> %s </p>' % cur_date
    return result


@app.route('/news') 
def all_the_news():
	colors= ['blue','green','red']
	try:
	    limit = int(request.args.get('limit', 'all'))
	except:
	    limit = 10
	color = request.args.get('color') if request.args.get('color') in colors else 'black'
	for item in request.args:
		print(item)
		print(request.args.get(item))
	return '<h1 style="color: %s">News: <small>%s</small></h1>'  % (color,limit)

@app.route('/news/<int:news_id>') 
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>'
        result = result % news_to_show[0]
        return result
    else:
        abort(404)

if __name__ == '__main__':
    app.run(port=5010,debug=True)