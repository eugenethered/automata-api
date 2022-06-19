import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder

from apiautomata.server.AutomataAPIServer import AutomataAPIServer

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'API_SERVER_HOST': '127.0.0.1',
        'API_SERVER_PORT': 8000,
        'MISSING_KEY': '<MARKET>:missing',
        'INSTRUMENT_EXCHANGES_KEY': '<MARKET>:exchange:instruments',
        'EXCHANGE_TRANSFORMATIONS_KEY': '<MARKET>:transformation:exchange',
        'TRADE_TRANSFORMATIONS_KEY': '<MARKET>:transformation:trade',
        'EXCHANGE_RATE_TIMESERIES_KEY': '<MARKET>:time-series:exchange-rate:{}',
        'EXCHANGE_RATE_TIMESERIES_RETENTION': 360000,
        'PROCESS_RUN_PROFILE_KEY': '{}:process:run-profile:{}',
        'PROCESS_KEY': '{}:process:status:{}',
        'PROCESS_RUN_COMMAND': 'echo "running: {process-name}"',
        'VERSION': '0.0.1'
    }

    logging.basicConfig(level=logging.DEBUG)

    logging.getLogger('RedisCacheProvider').setLevel(logging.DEBUG)
    logging.getLogger('ExchangeTransformRepository').setLevel(logging.DEBUG)
    logging.getLogger('MissingRepository').setLevel(logging.DEBUG)

    RedisCacheHolder(options)

    server = AutomataAPIServer(options)
    server.run()
