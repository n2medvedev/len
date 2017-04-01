import requests

def get_open_name(url):
	result = requests.get(url)
	if result.status_code == 200:
	    return result.json()
	else:
		return ('что-то не так: код доступа '+str(result.status_code))

if __name__ == '__main__':
	data = get_open_name('http://api.data.mos.ru/v1/datasets/2009/rows')
	for el_data in data:
	    print(el_data)
