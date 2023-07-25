import unittest
from currency_rates_func import currency_rates


class TestCurrencyRates(unittest.TestCase):
    def test_correct_val(self):
        resp = currency_rates('AUD', '2010-03-02')
        self.assertEqual(resp, "AUD (Австралийский доллар): 26,9101")

    def test_wrong_val(self):
        with self.assertRaises(ValueError):
            resp = currency_rates('AAAAAAA', '2010-03-02')
