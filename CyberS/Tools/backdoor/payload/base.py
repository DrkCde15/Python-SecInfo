class BasePayload:
    name = "Default"
    code = None
    active = False
    conf = None
    stager_path = ""

    def set_handler(self, ip, port):
        data = {'SERVER': ip, 'PORT': port}
        self.set_code(data)

    def set_activated(self, status):
        self.active = status

    def read_stager(self):
        with open(self.stager_path, 'r') as f:
            return f.read()

    def set_code(self, values={}):
        self.code = self.read_stager().format(**values)

    def get_code(self):
        return self.code

    def getName(self):
        return self.name