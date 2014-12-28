"""Main entrypoint to ipsync."""

import logging
import requests
import ipaddress

from ipsync import providers


def resolve_ip():
    """Resolve the external IP address of this machine.

    :return: External IP address as a string
    """
    logger = logging.getLogger()

    response = requests.get('https://icanhazip.com/')
    if response.status_code == requests.codes['ok']:
        try:
            ip = ipaddress.ip_address(response.text.strip())
        except ValueError as error:
            logger.error('Could not receive a valid IP address\n%s', error.args)
            return None

        logger.info('Received IP address %s', str(ip))
        return str(ip)
    else:
        return None

if __name__ == '__main__':
    test = providers.DnsProvider('rax', 'bla')
    test.update_records()
