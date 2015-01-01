# pylint: disable=C0111,R0903
from ip_sync.test import TestBase
from ip_sync import providers


class TestProviders(TestBase):
    def test_get_providers(self):
        providers.get_provider('rax', self._config_yaml)
