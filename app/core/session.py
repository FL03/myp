from web3 import Web3, HTTPProvider

from .config import Settings
from .constants import Constants
from ..utils.generators import tokens
from ..utils.ledgering import timestamp


class Session(object):
    constants: Constants = Constants()
    key: str = tokens.generate_token().token
    provider: Web3
    settings: Settings = Settings()
    timestamp: str = timestamp()

    def __init__(self):
        self.provider = Web3(HTTPProvider(self.settings.providers[0].endpoint))


session: Session = Session()
