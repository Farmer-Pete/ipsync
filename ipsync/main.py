"""ipsync.

Usage:
    ipsync [-v|--version] [-h|--help] [-c FILE|--config=FILE] [--dry-run]
           <command>

Options:
    -h --help               Show this screen.
    -v --version            Show version.
    -c FILE --config=FILE   Configuration FILE to use [default: ~/.config/ipsync.conf]
    --dry-run               Run but don't make any changes.

Available commands:
    update                  Resolve current IP address and update all providers

"""

import logging
import requests
import ipaddress
import six
from docopt import docopt
from schema import Schema, Or, Use, SchemaError

from ipsync.version import __version__


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


def load_config():
    """Load the configuration yaml from disk."""
    pass


def main():
    """The main entrypoint to ipsync."""
    providers = {'rax', provider_update_rax}

    arguments = docopt(__doc__, version='ipsync %s' % __version__)
    schema = Schema({
        '--config': Or('~/.config/ipsync.conf',
                       Use(open, error='--config file must be readable')),
        object: object
    })
    try:
        arguments = schema.validate(arguments)
    except SchemaError as error:
        exit(error)

    print('args:')
    print(arguments)


if __name__ == '__main__':
    main()
    # read YAML
    # for each root key in YAML
    #   update_function = providers.get(key)
    #   if update_function:
    #     update_function(config_section)
