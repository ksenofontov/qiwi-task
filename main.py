import requests
import unittest
from pprint import pprint
import xmltodict


def cbr_cur_get(code, user_date):
    pars = {'date_req': user_date}
    r = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', params=pars)
    resp_dict = xmltodict.parse(r.text)
    for i in resp_dict['ValCurs']['Valute']:
        if i['CharCode'] == code:
            return i['Value']


resp = cbr_cur_get('USD', '02/03/2006')
pprint(resp)
