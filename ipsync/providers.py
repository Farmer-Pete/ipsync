import abc
import logging


class ProviderBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, config):
        logger = logging.getLogger(__name__)

        self.config = config
        if not self.check_dependencies():
            logger.error('dependencies not fulfilled')

    @abc.abstractmethod
    def __str__(self):
        return 'BaseProvider'

    @abc.abstractmethod
    def check_dependencies(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError()


class ProviderRax(ProviderBase):
    def __str__(self):
        return 'rax'

    def check_dependencies(self):
        return True

    def update(self):
        return


class ProviderFactory(object):
    _providers = {'rax': ProviderRax}

    def __str__(self):
        if self._active_provider:
            return str(self._active_provider)

    def __init__(self, api, config):
        logger = logging.getLogger(__name__)

        self._active_provider = self._providers.get(api, None)
        if not self._active_provider:
            logger.error('API provider {api} not found'.format(api=api))

        if not config:
            raise AttributeError('config cannot be None')

        self._active_provider = self._active_provider(config)
        logger.info('Registered provider: {provider}'.format(provider=self._active_provider))

    def update_records(self):
        logger = logging.getLogger(__name__)

        if not self._active_provider:
            logger.error('Provider is no longer registered')
            return None

        self._active_provider.update()
