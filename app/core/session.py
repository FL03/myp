from functools import lru_cache

from deta import Deta
from web3 import HTTPProvider, Web3

from app.core import constants, config
from app.utils.date import timestamp


class Session(object):
    constants = constants.Constants()
    deta: Deta
    provider: Web3
    settings: config.Settings = config.get_settings()
    timestamp: str = timestamp()

    def __init__(self):
        self.deta = Deta(self.settings.deta_key)
        self.provider = Web3(HTTPProvider(self.settings.provider.endpoint))


@lru_cache()
def get_session() -> Session: return Session()


session = get_session()
