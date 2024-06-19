import os
from config.bot_config import load_config


def test_config_loads_data_from_environment():
    result = {
        'TG_ADMIN_IDS': '1, 2, 3, 5',
        'TG_BOT_TOKEN': '12345:abcd'
    }
    for key in result.keys():
        os.environ[key] = result[key]
    config = load_config()
    assert config.tg.token == result['TG_BOT_TOKEN']
    assert config.tg.admin_ids == [1, 2, 3, 5]
