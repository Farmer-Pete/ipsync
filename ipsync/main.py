"""Main entrypoint to ipsync."""

import logging
from ipsync import providers

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    test = providers.DnsProvider('rax', 'bla')
    test.update_records()
