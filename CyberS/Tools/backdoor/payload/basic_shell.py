from core.common.config import Settings
from payload.base import BasePayload

class BasicShell(BasePayload):
    name = "Basic"
    code = None
    active = False
    conf = Settings()
    stager_path = "./stagers/basic.ps1"

    @staticmethod
    def get_name():
        return BasicShell.name

    def __init__(self):
        self.set_activated(self.conf.get_payload_status(self.name))