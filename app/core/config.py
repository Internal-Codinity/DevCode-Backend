from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Codex Backend"
    debug: bool = True
    secret_key: str = "change-me"
    database_url: str = "sqlite:///./codex.db"
    access_token_expire_minutes: int = 60


settings = Settings()



# application configuration, app name, debug mode, secret key, database url, access token expire time, environment variables, config file, config management