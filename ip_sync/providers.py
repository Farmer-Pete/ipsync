# pylint: disable=R0903
"""Defines cloud providers and exposes ProviderFactory."""

import abc
import logging


class AbstractProvider(object):

    """Used to define the provider interface, all providers must inherit from GenericProvider."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update_ip(self, ip):
        """Update the provider's DNS records with the new IP address.

        This must be overridden by the provider class

        :param: ip: New IP address to update at the provider
        :return: None
        """
        pass


class GenericProvider(AbstractProvider):

    """Set the config data when a provider is instantiated.

    All providers must inherit from this class.
    """

    def __init__(self, name, config):
        """Create a new provider.

        :param name:
        :param config: Provider specific config
        :return:
        """
        self._name = name
        self._config = config

    @abc.abstractmethod
    def update_ip(self, ip):
        """Update the provider's DNS records with the new IP address.

        This must be overridden by the provider class

        :param: ip: New IP address to update at the provider
        :return: None
        """
        pass


class InvalidProvider(GenericProvider):

    """Used when no provider could be found matching the config yaml."""

    def update_ip(self, ip):
        """Log to file and do nothing."""
        logger = logging.getLogger()

        logger.error('Unable to find provider %s', self._name)
        return False


class Rackspace(GenericProvider):

    """Rackspace cloud provider. Allows updating IP address of Rackspace Cloud DNS."""

    def update_ip(self, ip):
        """Update the IP address stored within a Rackspace Cloud DNS domain.

        This function will create the hostname if it does not already exist.

        :param ip:
        :return:
        """
        logger = logging.getLogger()

        logger.debug('RAX config: %s', self._config)
        logger.info('Updating RAX with IP %s', ip)

        return False


def get_provider(name, config):
    """Return a provider class which will update the IP address at that specific provider.

    :param name: Name of the provider from the yaml config.
    :param config: Parsed data from the yaml config.
    :return: Provider class.
    """
    for subclass in GenericProvider.__subclasses__():  # pylint: disable=E1101
        if subclass.__name__.lower() == name.lower():
            provider = subclass(name, config)
            break
    else:
        provider = InvalidProvider(name, config)

    return provider
