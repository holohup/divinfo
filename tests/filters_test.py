from config.bot_config import load_config
from filters.is_admin import IsAdmin


def test_is_admin_filter(project_settings):
    config = load_config()
    assert IsAdmin(100) is True
