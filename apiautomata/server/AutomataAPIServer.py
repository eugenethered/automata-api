import uvicorn

from apiautomata.holder.PlainItemHolder import PlainItemHolder


class AutomataAPIServer:

    def __init__(self, options):
        self.options = options
        self.port = options['API_SERVER_PORT']
        self.init_dependencies()

    def init_dependencies(self):
        plain_item_holder = PlainItemHolder()
        plain_item_holder.add('version', self.options['VERSION'])

    def run(self):
        uvicorn.run('apiautomata.API:app', port=self.port, access_log=False)
