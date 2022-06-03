import logging

from apiautomata.server.AutomataAPIServer import AutomataAPIServer

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'API_SERVER_PORT': 8000,
        'VERSION': '0.0.1'
    }

    logging.basicConfig(level=logging.DEBUG)

    server = AutomataAPIServer(options)
    server.run()
