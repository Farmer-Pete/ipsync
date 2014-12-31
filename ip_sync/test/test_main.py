# pylint: disable=C0111,R0903
import unittest
from mock import patch
from ipaddress import IPv4Address, IPv6Address
import six
import io

from ip_sync import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self._config_yaml = """rax:
  api_username: test
  api_key: 123abc
  domains:
    - test.com
    - www.test.com

namecheap:
  test.com:
    hostname: www
    password: password

  example.com:
    hostname: test
    password: 123456"""

    @patch('requests.get')
    def test_resolve_ipv4(self, request_mock):
        ip = '127.0.0.1'

        request_mock.return_value.status_code = 200
        request_mock.return_value.text = '%s\n' % ip

        self.assertEquals(main.resolve_ip(), IPv4Address(six.u(ip)))

    @patch('requests.get')
    def test_resolve_ipv6(self, request_mock):
        for ip in ['2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                   '2001:0db8:85a3::8a2e:0370:7334',
                   '::1']:
            request_mock.return_value.status_code = 200
            request_mock.return_value.text = '%s\n' % ip

            self.assertEquals(main.resolve_ip(), IPv6Address(six.u(ip)))

    @patch('requests.get')
    def test_resolve_ip_returns_none_on_error(self, request_mock):
        request_mock.return_value.status_code = 500
        request_mock.return_value.text = 'An error occurred'

        self.assertEquals(main.resolve_ip(), None)

    @patch('requests.get')
    def test_resolve_ip_returns_none_on_invalid_data(self, request_mock):
        request_mock.return_value.status_code = 200
        request_mock.return_value.text = 'some random data\n'

        self.assertEquals(main.resolve_ip(), None)

    def test_load_config(self):
        config_file = io.StringIO(six.u(self._config_yaml))
        config_file.name = 'test_config.yml'
        config_data = main.load_config(config_file)
        self.assertIsNotNone(config_data.get('rax'))
        self.assertIsNotNone(config_data.get('namecheap'))
        self.assertIsNotNone(config_data['rax'].get('api_username'))
        self.assertIsNotNone(config_data['namecheap'].get('test.com'))
        self.assertIsNotNone(config_data['namecheap']['test.com'].get('hostname'))
