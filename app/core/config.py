import glob
import json
import pathlib
from typing import Any, Dict, Optional

from pydantic import BaseModel, BaseSettings


def json_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    encoding = settings.__config__.env_file_encoding
    return json.loads(pathlib.Path(glob.glob("**/config.json")[0]).read_text(encoding))


class Application(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    token: str


class Provider(BaseModel):
    endpoint: str


class Settings(BaseSettings):
    application: Application
    deta_key: str
    deta_name: str
    provider: Provider

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return init_settings, json_config_settings_source, env_settings, file_secret_settings
