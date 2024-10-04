import requests
from bs4 import BeautifulSoup
import time
from typing import Dict


headers: Dict[str, ...] = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_full_page(url: str, headers: Dict[str, ...]) -> float:
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll('span', {'class': "DFlfde", "class": "SwHCTb", 'data-precision': "2"})
    rate = convert[0].text
    return float(rate.replace(',', '.'))


EURO_UAH_URL: str = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE&rlz=1C1IXYC_ruUA983UA983&sxsrf=AJOqlzWGjwLHzJHEhO0MlIhp8lMAzq2CYg%3A1675756307966&ei=EwPiY4HWOpCVrwSip6fQBQ&oq=tdhj&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMhAIABCABBAKEAEQKhBGEIICMgoIABCABBCxAxAKMg0IABCABBCxAxCDARAKMg0IABCABBCxAxCDARAKMgwILhCABBDUAhAKEAEyCAgAELEDEIMBMhYILhCABBCxAxCDARDHARDRAxDUAhAKMgkIABCABBAKEAEyCggAEIAEELEDEAoyCQguEIAEEAoQAToHCCMQ6gIQJzoECCMQJzoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgUIABCABDoICAAQgAQQsQM6CwguEIAEEMcBEK8BOgsIABCABBAKEAEQKjoHCAAQgAQQCkoECEEYAEoECEYYAFAAWIYGYIoWaAFwAXgAgAFUiAHGApIBATSYAQCgAQGwAQrAAQE&sclient=gws-wiz-serp'
DOLLAR_UAH_URL: str = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&rlz=1C1IXYC_ruUA983UA983&sxsrf=AJOqlzXC55imZZegR3OdkFA1U377T2MSjw%3A1675756384735&ei=YAPiY-OMKefmrgSero-oAg&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMg8IABCxAxCDARBDEEYQggIyBwgAELEDEEMyCggAELEDEIMBEEMyBwgAELEDEEMyCggAELEDEIMBEEMyCwgAEIAEELEDEIMBMhAIABCABBAUEIcCELEDEIMBMgQIABBDMgQIABBDMggIABCABBCxAzoKCAAQRxDWBBCwAzoNCAAQRxDWBBDJAxCwAzoICAAQkgMQsAM6BwgAELADEEM6BAgjECc6DQgAEIAEEBQQhwIQsQM6CAgAELEDEIMBOgUIABCABDoJCCMQJxBGEIICOgoIABCABBAUEIcCOggILhCxAxCDAToHCCMQ6gIQJzoRCC4QgAQQsQMQgwEQxwEQ0QM6DgguEIMBEMcBELEDENEDOgsILhCABBDHARDRAzoKCC4QxwEQ0QMQJzoHCAAQyQMQQ0oECEEYAEoECEYYAFDfBFjhG2D8JWgDcAB4AIABVIgBuQWSAQE5mAEAoAEBsAEKyAEKwAEB&sclient=gws-wiz-serp'
PLN_UAH_URL: str = 'https://www.google.com/search?q=%D0%B7%D0%BB%D0%BE%D1%82%D1%8B%D0%B9+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&rlz=1C1IXYC_ruUA983UA983&sxsrf=AJOqlzX4PDSpkyq0bTQFvxODhPSzFUY2sg%3A1675759299758&ei=ww7iY6P5Le36qwGs0L74AQ&oq=%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F+%D0%B7%D0%BB%D0%BE%D1%82%D0%B0%D1%8F&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgBMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADSgQIQRgASgQIRhgAUABYAGCnD2gBcAF4AIABAIgBAJIBAJgBAMgBCMABAQ&sclient=gws-wiz-serp'

current_datetime = time.ctime(time.time())

EURO = get_full_page(EURO_UAH_URL, headers)
DOLLAR = get_full_page(DOLLAR_UAH_URL, headers)
PLN = get_full_page(PLN_UAH_URL, headers)


welcome_text: str = 'Welcome to "Privat24 Bank".'
print(welcome_text)

print(f'Currency exchange for {current_datetime}')
print(f'1$ --> {DOLLAR} UAH')
print(f'1€--> {EURO} UAH')
print(f'1PLN --> {DOLLAR} UAH')

exchange_rates: Dict[str, float] = {
    '$': float(DOLLAR),
    '€': float(EURO),
    'PLN': float(PLN)
}

while True:
    try:

        operation = str(input("If you want exchange currency enter 'exchange' or 'Exit' if you want to leave the bank. "))

        if operation == 'exchange':
            choose_currency = str(input('SELECT : $, PLN , € or UAH: '))
            select_sum = int(input('Enter the amount to exchange: '))
        elif operation == 'Exit':
            break

        if choose_currency in exchange_rates:
            print(select_sum * round(exchange_rates[choose_currency], 2), 'UAH')
        elif choose_currency == 'UAH':
            print(select_sum / round(exchange_rates['PLN'], 2), 'PLN')
            print(select_sum / round(exchange_rates['$'], 2), '$')
            print(select_sum / round(exchange_rates['€'], 2), '€')
        else:
            print('Invalid currency selected.')
    except ValueError:
        print('Choose number')
