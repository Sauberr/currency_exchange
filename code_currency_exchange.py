import requests
from bs4 import BeautifulSoup
from datetime import datetime

EURO_GRV = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE&rlz=1C1IXYC_ruUA983UA983&sxsrf=AJOqlzWGjwLHzJHEhO0MlIhp8lMAzq2CYg%3A1675756307966&ei=EwPiY4HWOpCVrwSip6fQBQ&oq=tdhj&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMhAIABCABBAKEAEQKhBGEIICMgoIABCABBCxAxAKMg0IABCABBCxAxCDARAKMg0IABCABBCxAxCDARAKMgwILhCABBDUAhAKEAEyCAgAELEDEIMBMhYILhCABBCxAxCDARDHARDRAxDUAhAKMgkIABCABBAKEAEyCggAEIAEELEDEAoyCQguEIAEEAoQAToHCCMQ6gIQJzoECCMQJzoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgUIABCABDoICAAQgAQQsQM6CwguEIAEEMcBEK8BOgsIABCABBAKEAEQKjoHCAAQgAQQCkoECEEYAEoECEYYAFAAWIYGYIoWaAFwAXgAgAFUiAHGApIBATSYAQCgAQGwAQrAAQE&sclient=gws-wiz-serp'

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

current_datetime = datetime.now()

full_page = requests.get(EURO_GRV, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll('span', {'class': "DFlfde", "class": "SwHCTb", 'data-precision': "2"})

euro = convert[0].text

EURO = euro.replace(',', '.')

DOLLAR_GRV = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&rlz=1C1IXYC_ruUA983UA983&sxsrf=AJOqlzXC55imZZegR3OdkFA1U377T2MSjw%3A1675756384735&ei=YAPiY-OMKefmrgSero-oAg&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMg8IABCxAxCDARBDEEYQggIyBwgAELEDEEMyCggAELEDEIMBEEMyBwgAELEDEEMyCggAELEDEIMBEEMyCwgAEIAEELEDEIMBMhAIABCABBAUEIcCELEDEIMBMgQIABBDMgQIABBDMggIABCABBCxAzoKCAAQRxDWBBCwAzoNCAAQRxDWBBDJAxCwAzoICAAQkgMQsAM6BwgAELADEEM6BAgjECc6DQgAEIAEEBQQhwIQsQM6CAgAELEDEIMBOgUIABCABDoJCCMQJxBGEIICOgoIABCABBAUEIcCOggILhCxAxCDAToHCCMQ6gIQJzoRCC4QgAQQsQMQgwEQxwEQ0QM6DgguEIMBEMcBELEDENEDOgsILhCABBDHARDRAzoKCC4QxwEQ0QMQJzoHCAAQyQMQQ0oECEEYAEoECEYYAFDfBFjhG2D8JWgDcAB4AIABVIgBuQWSAQE5mAEAoAEBsAEKyAEKwAEB&sclient=gws-wiz-serp'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

full_page = requests.get(DOLLAR_GRV, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll('span', {'class': "DFlfde", "class": "SwHCTb", 'data-precision': "2"})

dollar = convert[0].text

DOLLAR = dollar.replace(',', '.')

PLN_GRV = 'https://www.google.com/search?q=%D0%B7%D0%BB%D0%BE%D1%82%D1%8B%D0%B9+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&rlz=1C1IXYC_ruUA983UA983&sxsrf=AJOqlzX4PDSpkyq0bTQFvxODhPSzFUY2sg%3A1675759299758&ei=ww7iY6P5Le36qwGs0L74AQ&oq=%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F+%D0%B7%D0%BB%D0%BE%D1%82%D0%B0%D1%8F&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgBMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADSgQIQRgASgQIRhgAUABYAGCnD2gBcAF4AIABAIgBAJIBAJgBAMgBCMABAQ&sclient=gws-wiz-serp'


headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

full_page = requests.get(PLN_GRV, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll('span', {'class': "DFlfde", "class": "SwHCTb", 'data-precision': "2"})

pln = convert[0].text

PLN = pln.replace(',', '.')


welcome_text = 'Welcome to "Privat24 Bank". Choose a service: exchange rate or currency exchange'
print(welcome_text)

print(f'Currency exchange for {current_datetime}')
print(f'1$ --> {dollar} GRV')
print(f'1€--> {euro} GRV')
print(f'1PLN --> {pln} GRV')

while True:
	try:

		operation = str(input("Choose a service: currency exchange: "))

		if operation == 'currency exchange':
			choose_currency = str(input('SELECT : $, PLN or €: '))
			select_sum = int(input('Enter the amount to exchange: '))
			if choose_currency == '$':
				print(select_sum * round(float(DOLLAR), 2))
			if choose_currency == '€':
				print(select_sum * round(float(EURO), 2))
			if choose_currency == 'PLN':
				print(select_sum * round(float(PLN), 2))
	except ValueError:
		print('Choose number')
