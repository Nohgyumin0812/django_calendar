from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

####크롤링####
import requests
import bs4
import datetime as dt
############

"""
		loc = '09230740'
		url = 'https://weather.naver.com/today/%s' % (loc)
		raw = requests.get(url)
		html = bs4.BeautifulSoup(raw.text, 'html.parser')
		target = html.find('ul', {'class': 'week_list'})
		day_datas = target.find_all('div', {'class': 'day_data'})
		weather_lst = []

		for day_data in day_datas:
			date_data = day_data.find('span', {'class': 'date'})
			weather_inner = day_data.find_all('span', {'class': 'weather_inner'})
			for weathers in weather_inner:
				timeslot = weathers.find('span', {'class': 'timeslot'})
				weather = weathers.find('i', {'class': 'ico'})
				if timeslot.text == '오전':
					weather_lst.append([date_data.text, timeslot.text, weather.text])

		if day < dt.datetime.now().day:
			d = ''

		elif day <int(dt.datetime.now().day) + 1:
			d= weather_lst[0][2]

		elif day <int(dt.datetime.now().day) + 2:
			d= weather_lst[1][2]

		elif day <int(dt.datetime.now().day) + 3:
			d= weather_lst[2][2]

		elif day <int(dt.datetime.now().day) + 4:
			d= weather_lst[3][2]

		elif day <int(dt.datetime.now().day) + 5:
			d= weather_lst[4][2]

		elif day <int(dt.datetime.now().day) + 6:
			d= weather_lst[5][2]

		elif day <int(dt.datetime.now().day) + 7:
			d= weather_lst[6][2]

		elif day <int(dt.datetime.now().day) + 8:
			d= weather_lst[7][2]

		elif day <int(dt.datetime.now().day) + 9:
			d= weather_lst[8][2]

		elif day <int(dt.datetime.now().day) + 10:
			d= weather_lst[9][2]

		else:
			d = ''
	"""