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
        'VERSION': '0.0.1'
    }

    logging.basicConfig(level=logging.DEBUG)

    RedisCacheHolder(options)

    server = AutomataAPIServer(options)
    server.run()
