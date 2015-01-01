# pylint: disable=C0111,R0903
from ipaddress import IPv4Address
import six

from ip_sync.test import TestBase
from ip_sync import providers


class TestProviders(TestBase):
    def setUp(self):
        super(TestProviders, self).setUp()

    def test_get_invalid_provider(self):
        self.assertIsInstance(providers.get_provider('invalid-provider-123456', None),
                              providers.InvalidProvider)

    def test_get_providers(self):
        provider_data = {
            'invalid-provider-123456': (None, providers.InvalidProvider),
            'rackspace': (self._config_data.get('rackspace'), providers.Rackspace),
            'namecheap': (self._config_data.get('namecheap'), providers.Namecheap),
        }

        for name in self._config_data:
            self.assertIsNotNone(provider_data.get(name), 'No Provider exists for \'%s\'' % name)
            config, class_type = provider_data.get(name)
            result = providers.get_provider(name, config)

            self.assertIsInstance(result, class_type,
                                  'result \'%s\' is not an instance of \'%s\''
                                  % (result.__class__.__name__, class_type))

            self.assertEqual(result._name, name)  # pylint: disable=W0212
            self.assertEqual(result._config, config)  # pylint: disable=W0212

    def test_invalid_provider_update(self):
        provider = providers.get_provider('invalid-provider-1234', None)
        self.assertIsInstance(provider, providers.InvalidProvider)
        provider.update_ip(IPv4Address(six.u('127.0.0.1')))

    def test_rackspace_update(self):
        provider = providers.get_provider('rackspace', self._config_data['rackspace'])
        self.assertIsInstance(provider, providers.Rackspace)
        provider.update_ip(IPv4Address(six.u('127.0.0.1')))

    def test_namecheap_update(self):
        provider = providers.get_provider('namecheap', self._config_data['namecheap'])
        self.assertIsInstance(provider, providers.Namecheap)
        provider.update_ip(IPv4Address(six.u('127.0.0.1')))
