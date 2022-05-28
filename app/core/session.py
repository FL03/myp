from functools import lru_cache

import deta
from web3 import HTTPProvider, Web3

from app.core import constants, config
from app.utils.date import timestamp


class Session(object):
    constants = constants.Constants()
    database: deta.Deta.Base
    provider: Web3
    settings: config.Settings = config.get_settings()
    timestamp: str = timestamp()

    def __init__(self):
        self.db = deta.Deta(self.settings.deta_key).Base(self.settings.deta_name)
        self.provider = Web3(HTTPProvider(self.settings.provider.endpoint))


@lru_cache()
def get_session() -> Session: return Session()


session = get_session()
