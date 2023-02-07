import random
from aiogram import Bot, Dispatcher
from aiogram.types  import Message
from aiogram.filters import Text, Command

user: dict = {'in_game': False,
              'secret_number' : None,
              'attempts' : None,  #попытки
              'total_games': 0,
              'wins':0
              }

def get_random_number() -> int:
    return random.randint(1, 100)

bot_token: str ='5923154900:AAECR2DEtm_zLqnNzRsXy5Wzjm83RqYizDc'

bot: Bot=Bot(bot_token)
dp: Dispatcher=Dispatcher()

attamps: int=5

