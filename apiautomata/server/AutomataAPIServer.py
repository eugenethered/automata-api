import uvicorn


class AutomataAPIServer:

    def __init__(self, options):
        self.port = options['API_SERVER_PORT']

    def run(self):
        uvicorn.run('apiautomata.API:app', port=self.port, reload=True, access_log=False)
