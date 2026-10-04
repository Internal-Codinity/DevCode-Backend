from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Codex Backend"
    debug: bool = True
    secret_key: str = "change-me"
    database_url: str = "sqlite:///./codex.db"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()



# application configuration, app name, debug mode, secret key, database url, access token expire time, environment variables, config file, config management