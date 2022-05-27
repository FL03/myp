import glob
import json
import pathlib
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, BaseSettings


def json_config_settings_source(config: BaseSettings) -> Dict[str, Any]:
    encoding = config.__config__.env_file_encoding
    return json.loads(pathlib.Path(glob.glob("**/default.config.json")[0]).read_text(encoding))


class Database(BaseModel):
    name: str
    uri: str


class Project(BaseModel):
    name: str
    run_mode: str
    slug: str


class Provider(BaseModel):
    endpoint: str
    public: Optional[str]
    private: Optional[str]


class Server(BaseModel):
    host: str
    port: int
    reload: bool


class Settings(BaseSettings):
    databases: List[Database]
    project: Project
    providers: List[Provider]
    server: Server

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return init_settings, json_config_settings_source, env_settings, file_secret_settings
