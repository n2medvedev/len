import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
	    return result.json()
	else:
		return ('что-то не так: код доступа '+str(result.status_code))

if __name__ == '__main__':
	print(get_weather('http://api.openweathermap.org/data/2.5/weather?id=524901&appid=7625ce8a3c25d35969acfa3957fb8fc9&units=metric'))
