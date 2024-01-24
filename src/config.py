from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsLoadDotEnv:
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")

    DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class PydanticSettings(BaseSettings):
    MODE: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


# class PydanticSettingsConfig(BaseSettings):
#     MODE: str
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME: str
#
#     @property
#     def DB_URL(self):
#         return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
#
#     class Config:
#         env_file = ".env"


settings = PydanticSettings()


if __name__ == '__main__':
    sl = SettingsLoadDotEnv()
    print(sl.DB_URL)

    # pc = PydanticSettingsConfig()
    # print(pc.DB_URL)

    ps = PydanticSettings()
    print(ps.DB_URL)
