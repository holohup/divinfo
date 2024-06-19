from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg=TgBot(
            token=env('TG_BOT_TOKEN'),
            admin_ids=list(map(int, env.list('TG_ADMIN_IDS')))
        )
    )
