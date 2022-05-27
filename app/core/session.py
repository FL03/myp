import deta
from web3 import Web3, HTTPProvider

from .config import Settings
from .constants import Constants
from ..utils.ledgering import timestamp


class Session(object):
    constants: Constants = Constants()
    database: deta.Deta.Base
    provider: Web3
    settings: Settings = Settings()
    timestamp: str = timestamp()

    def __init__(self):
        self.db = deta.Deta(self.settings.deta_key).Base(self.settings.deta_name)
        self.provider = Web3(HTTPProvider(self.settings.provider.endpoint))


session: Session = Session()
