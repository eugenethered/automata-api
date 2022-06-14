import logging

import uvicorn
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository
from exchangerepo.repository.InstrumentExchangeRepository import InstrumentExchangeRepository
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository
from missingrepo.repository.MissingRepository import MissingRepository
from processrepo.repository.ProcessRunProfileRepository import ProcessRunProfileRepository

from apiautomata.holder.ItemHolder import ItemHolder


class AutomataAPIServer:

    def __init__(self, options):
        self.log = logging.getLogger(__name__)
        self.options = options
        self.host = options['API_SERVER_HOST']
        self.port = options['API_SERVER_PORT']
        self.init_dependencies()

    def init_dependencies(self):
        self.log.info('Initializing dependencies')
        item_holder = ItemHolder()
        item_holder.add(self.options['VERSION'], 'version')
        item_holder.add_entity(MissingRepository(self.options))
        item_holder.add_entity(InstrumentExchangeRepository(self.options))
        item_holder.add_entity(ExchangeTransformRepository(self.options))
        item_holder.add_entity(ExchangeRateRepository(self.options))
        item_holder.add_entity(ProcessRunProfileRepository(self.options))

    def run(self):
        self.log.info('Running')
        uvicorn.run('apiautomata.API:app', host=self.host, port=self.port, access_log=False)
