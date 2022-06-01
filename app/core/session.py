from deta import Deta
from web3 import HTTPProvider, Web3

from app.core import constants, config
from app.utils.date import timestamp


class Session(object):
    constants: constants.Constants
    deta: Deta
    provider: Web3
    settings: config.Settings = config.get_settings()
    timestamp: str = timestamp()

    def __init__(self):
        self.constants = constants.Constants(base_url=self.settings.base_url)
        self.deta = Deta(self.settings.deta_access_token)
        self.provider = Web3(HTTPProvider(self.settings.provider.endpoint))


session: Session = Session()
