
import os,path,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import unittest
from io import BytesIO
from source.currency_exchanger import CurrencyExchanger
from unittest.mock import patch, Mock
from utils import get_mock_country_api_response


class TestCurrencyExchanger(unittest.TestCase):
    
    def setUp(self):
        self.currency_exchanger = CurrencyExchanger(target_currency="KRW")
        self.expect_response = get_mock_country_api_response()
        
    @patch('source.currency_exchanger.requests')
    def test_get_currency_rate(self, mock_requests):
        mock_requests.get.return_value = self.expect_response
        
        self.currency_exchanger.get_currency_rate()
        
        mock_requests.get.called_with("https://coc-kku-bank.com/foreign-exchange?from=THB&to=KRW")
        mock_requests.get.assert_called_once()
        
        self.assertIsNotNone(self.currency_exchanger.api_response)
        self.assertEqual(self.currency_exchanger.api_response, self.expect_response.json())
        
    @patch('source.currency_exchanger.requests')
    def test_get_currency_exchange(self, mock_requests):
        mock_requests.get.return_value = self.expect_response
        
        self.result = self.currency_exchanger.currency_exchange(100)
        
        mock_requests.get.called_with("https://coc-kku-bank.com/foreign-exchange?from=THB&to=KRW")
        mock_requests.get.assert_called_once()
        
        self.assertIsNotNone(self.result)
        self.assertEqual(self.result, 3869)
        
        
        
if __name__ == '__main__':
    unittest.main()