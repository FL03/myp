from functools import lru_cache

import deta
from web3 import HTTPProvider, Web3

from .config import Settings, get_settings
from .constants import Constants
from ..utils.ledgering import timestamp


class Session(object):
    constants: Constants = Constants()
    database: deta.Deta.Base
    provider: Web3
    settings: Settings = get_settings()
    timestamp: str = timestamp()

    def __init__(self):
        self.db = deta.Deta(self.settings.deta_key).Base(self.settings.deta_name)
        self.provider = Web3(HTTPProvider(self.settings.provider.endpoint))


@lru_cache()
def get_session() -> Session: return Session()


session = get_session()
