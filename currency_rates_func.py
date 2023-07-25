import requests
from pprint import pprint
import xmltodict
from datetime import datetime


def currency_rates(code, date):
    formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")
    pars = {'date_req': formatted_date}
    r = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', params=pars)
    resp_dict = xmltodict.parse(r.text)
    for i in resp_dict['ValCurs']['Valute']:
        if i['CharCode'] == code:
            return f"{i['CharCode']} ({i['Name']}): {i['Value']}"
        else:
            raise ValueError(f"Код {code} не найден! Попробуйте другой код")




