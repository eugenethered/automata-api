import unittest

from apiautomata.server.AutomataAPIServer import AutomataAPIServer


class AutomataAPIServerTestCase(unittest.TestCase):

    def test_should_set_host_and_port_of_api_server(self):
        options = {
            'IGNORE_INIT_DEPENDENCIES': True,
            'API_SERVER_HOST': '127.0.0.1',
            'API_SERVER_PORT': 8000
        }
        api_sever = AutomataAPIServer(options)
        self.assertEqual(api_sever.host, '127.0.0.1')
        self.assertEqual(api_sever.port, 8000)


if __name__ == '__main__':
    unittest.main()
