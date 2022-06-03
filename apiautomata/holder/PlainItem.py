class PlainItem:

    def __init__(self):
        self.items = {}

    def add(self, name, value):
        self.items[name] = value

    def get(self, name):
        return self.items[name]
