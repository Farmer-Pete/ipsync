# pylint: disable=C0111,R0903
import unittest
from mock import patch
from ipaddress import IPv4Address, IPv6Address
import six

from ipsync import main


class TestMain(unittest.TestCase):
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
