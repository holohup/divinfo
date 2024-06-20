import os
from config.bot_config import load_config


def test_config_loads_data_from_environment(project_settings):
    for key in project_settings.keys():
        os.environ[key] = project_settings[key]
    config = load_config()
    assert config.tg.token == project_settings['TG_BOT_TOKEN']
    assert config.tg.admin_ids == [1, 2, 3, 5]
