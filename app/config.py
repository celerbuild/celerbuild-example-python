from pydantic_settings import BaseSettings
from typing import Literal
from pydantic import ConfigDict

class Settings(BaseSettings):
    app_name: str = "CelerBuild Example Python"
    version: str = "1.0.0"
    port: int = 8084
    env: Literal["development", "production"] = "development"
    debug: bool = True
    log_level: str = "debug"

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False  # Environment variable names are case insensitive
    )

# Create a global settings instance
settings = Settings()