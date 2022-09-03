import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithTimeSeries import RedisCacheProviderWithTimeSeries
from core.environment.EnvironmentVariables import EnvironmentVariables
from logger.ConfigureLogger import ConfigureLogger

from apiautomata.server.AutomataAPIServer import AutomataAPIServer


def start():
    ConfigureLogger()

    environment_variables = EnvironmentVariables()

    log = logging.getLogger('Automata API')
    log.info(f'Automata API starting')

    RedisCacheHolder(environment_variables.options, held_type=RedisCacheProviderWithTimeSeries)

    server = AutomataAPIServer(environment_variables.options)
    server.run()


if __name__ == '__main__':
    start()
