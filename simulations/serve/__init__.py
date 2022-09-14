import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from timeseries.holder.InfluxDBHolder import InfluxDBHolder

from apiautomata.server.AutomataAPIServer import AutomataAPIServer

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '127.0.0.1',
        'REDIS_SERVER_PORT': 6379,
        'API_SERVER_HOST': '127.0.0.1',
        'API_SERVER_PORT': 8000,
        'MISSING_KEY': '<MARKET>:mv:missing',
        'INSTRUMENT_EXCHANGES_KEY': '<MARKET>:exchange:mv:instruments',
        'EXCHANGE_TRANSFORMATIONS_KEY': '<MARKET>:transformation:mv:exchange',
        'INFLUXDB_SERVER_ADDRESS': '127.0.0.1',
        'INFLUXDB_SERVER_PORT': 8086,
        'INFLUXDB_AUTH_TOKEN': 'q3cfJCCyfo4RNJuyg72U-3uEhrv3qkKQcDOesoyeIDg2BCUpmn-mjReqaGwO7GOebhd58wYVkopi5tcgCj8t5w==',
        'INFLUXDB_AUTH_ORG': 'persuader-technology',
        'INFLUXDB_BUCKET': 'automata',
        'EXCHANGE_RATE_TIMESERIES_KEY': 'exchange-rate',
        'TRADE_TRANSFORMATIONS_KEY': '<MARKET>:transformation:mv:trade',
        'PROCESS_RUN_PROFILE_KEY': '<MARKET>:process:mv:run-profile',
        'PROCESS_KEY': '<MARKET>:process:mv:status',
        'PROCESS_RUN_COMMAND': 'echo "running: {process-name}"',
        'AUTH_INFO_KEY': '<MARKET>:auth:info',
        'VERSION': '0.0.1'
    }

    logging.basicConfig(level=logging.DEBUG)

    logging.getLogger('RedisCacheProvider').setLevel(logging.DEBUG)
    logging.getLogger('ExchangeTransformRepository').setLevel(logging.DEBUG)
    logging.getLogger('MissingRepository').setLevel(logging.DEBUG)

    RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
    InfluxDBHolder(options)

    server = AutomataAPIServer(options)
    server.run()
