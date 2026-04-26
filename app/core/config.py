from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.
    """

    # The default values for these settings are suitable for local development.
    # For production, these should be set via environment variables.
    APP_NAME: str = "Financial Planning App"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "A FastAPI application for financial planning."
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
