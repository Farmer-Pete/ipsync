# pylint: disable=C0111,R0903
import unittest
from ipsync import providers


class TestDnsProvider(unittest.TestCase):
    def test_dnsprovider_invalid_provider(self):
        provider = providers.DnsProvider('invalid-provider', 'random data')
        self.assertEquals(provider.update_records(), None)

    def test_invalid_config_raises_error(self):
        self.assertRaises(AttributeError, providers.DnsProvider, 'rax', None)
