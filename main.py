import requests
import unittest
from pprint import pprint
import xmltodict
from datetime import datetime


def cbr_cur_get(code, user_date):
    date_object = datetime.strptime(user_date, "%Y-%m-%d").strftime("%d-%m-%Y")
    pars = {'date_req': date_object}
    r = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', params=pars)
    resp_dict = xmltodict.parse(r.text)
    for i in resp_dict['ValCurs']['Valute']:
        if i['CharCode'] == code:
            return f"{i['CharCode']} ({i['Name']}): {i['Value']}"


resp = cbr_cur_get('USD', '2007-03-02')
pprint(resp)
