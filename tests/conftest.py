import pytest


@pytest.fixture
def project_settings():
    return {
        'TG_ADMIN_IDS': '1, 2, 3, 5',
        'TG_BOT_TOKEN': '12345:abcd'
    }
