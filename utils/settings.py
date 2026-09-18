from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_CONNECTION:str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    SECRET_KEY : str
    ALGORITHM : str

settings = Settings()