"""Main entrypoint to ipsync."""

import logging
import requests
import ipaddress
import six


def resolve_ip():
    """Resolve the external IP address of this machine.

    :return: External IP address
    """
    logger = logging.getLogger()

    response = requests.get('https://icanhazip.com/')
    if response.status_code == requests.codes['ok']:
        try:
            ip = ipaddress.ip_address(six.u(response.text.strip()))
        except ValueError as error:
            logger.error('Could not receive a valid IP address: %s', error.args)
            return None

        logger.info('Received IP address %s', ip)
        return ip
    else:
        return None


def provider_update_rax():
    """Use Pyrax to update DNS records configured within Rackspace Cloud DNS.

    If the domains do not already exist, this method will attempt to create them.
    If the records within the domain do not exist, this method will attempt to create them.

    :return: None
    """
    pass

if __name__ == '__main__':
    providers = {'rax', provider_update_rax}

    # read YAML
    # for each root key in YAML
    #   update_function = providers.get(key)
    #   if update_function:
    #     update_function(config_section)
