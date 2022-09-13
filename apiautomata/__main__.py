import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from core.environment.EnvironmentVariables import EnvironmentVariables
from logger.ConfigureLogger import ConfigureLogger
from timeseries.holder.InfluxDBHolder import InfluxDBHolder

from apiautomata.server.AutomataAPIServer import AutomataAPIServer


def start():
    ConfigureLogger()

    environment_variables = EnvironmentVariables()

    log = logging.getLogger('Automata API')
    log.info(f'Automata API starting')

    RedisCacheHolder(environment_variables.options, held_type=RedisCacheProviderWithHash)

    InfluxDBHolder(environment_variables.options)

    server = AutomataAPIServer(environment_variables.options)
    server.run()


if __name__ == '__main__':
    start()
