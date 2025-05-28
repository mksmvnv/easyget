import yaml

from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Personal(BaseModel):
    token: str
    admin_id: int


class Logistics(BaseModel):
    sneakers: int
    jackets: int
    other: int
    china: int
    fee: int


class Links(BaseModel):
    api: str
    home: str
    reviews: str


class Settings(BaseSettings):
    personal: Personal
    logistics: Logistics
    links: Links

    model_config = SettingsConfigDict(validate_default=True)

    @classmethod
    def from_yaml(cls, path: Path):
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        with path.open("r", encoding="utf-8") as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing YAML file: {e}")
        return cls(**data)


config_path = Path(__file__).parent / "config.yaml"

settings = Settings.from_yaml(config_path)
