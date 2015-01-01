# pylint: disable=C0111,R0903
from ip_sync.test import TestBase
from ip_sync import providers


class TestProviders(TestBase):
    def setUp(self):
        super(TestProviders, self).setUp()

    def test_get_providers(self):
        for provider in self._config_data:
            class_name = providers.get_provider(provider, self._config_data).__class__.__name__
            self.assertEqual(provider.lower(), class_name.lower(),
                             'Provider \'%s\' does not match \'%s\'' % (provider, class_name))
