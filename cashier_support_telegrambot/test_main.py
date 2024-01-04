
from aiogram import Bot, Dispatcher
from create_bot import dp
import admin
from main import on_startup

@pytest.fixture
async def bot():
    return Bot(token='6108069166:AAGP7r4ztRgOkylYcxdKTZtct7rlWkaug2U')

@pytest.fixture
async def dispatcher(bot):
    dp = Dispatcher(bot)
    return dp

@pytest.mark.asyncio
async def test_on_startup(dispatcher):
    await on_startup(None)
    # Add your assertions here

@pytest.mark.asyncio
async def test_bot_token(bot):
    assert bot.token == '6108069166:AAGP7r4ztRgOkylYcxdKTZtct7rlWkaug2U'

@pytest.mark.asyncio
async def test_dispatcher(dispatcher):
    # Add your assertions here

    if __name__ == '__main__':
        pytest.main()