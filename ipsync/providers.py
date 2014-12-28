"""The providers module abstracts the different DNS providers away from the main application."""

import logging


def provider_update_rax(config):
    """Use Pyrax to update DNS records configured within Rackspace Cloud DNS.

    If the domains do not already exist, this method will attempt to create them.
    If the records within the domain do not exist, this method will attempt to create them.

    :return: None
    """
    return config


class DnsProvider(object):

    """DnsProvider abstracts the provider implementations from the main application."""

    _providers = {'rax': provider_update_rax}

    def __str__(self):
        """Return the name of the current active provider.

        :return: String
        """
        if self._active_provider:
            for key, value in self._providers:
                if value is self._active_provider:
                    return key

        return 'DnsProvider'

    def __init__(self, api, config):
        """Instantiate a new DnsProvider and configure the active provider.

        :param api: Provider name, one of: 'rax', 'namecheap'
        :param config: YAML configuration section relevant to this provider
        :return: Instance of DnsProvider configured to the correct provider
        """
        logger = logging.getLogger(__name__)

        self._active_provider = self._providers.get(api, None)
        if not self._active_provider:
            logger.error('API provider %s not found', api)

        if not config:
            raise AttributeError('config cannot be None')
        self._config = config

        logger.info('Registered provider: %s', self)

    def resolve_ip(self):
        """.

        :return:
        """
        pass

    def update_records(self):
        """Update the DNS records using the current provider.

        :return:None
        """
        logger = logging.getLogger(__name__)

        if not self._active_provider:
            logger.error('Provider is no longer registered')
            return None

        return self._active_provider()
