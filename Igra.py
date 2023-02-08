import random
from aiogram import Bot, Dispatcher
from aiogram.types  import Message
from aiogram.filters import Text, Command

'''
user: dict = {'in_game': False,
              'secret_number' : None,
              'attempts' : None,  #попытки
              'total_games': 0,
              'wins':0
              }
'''

def get_random_number() -> int:
    return random.randint(1, 100)

bot_token: str ='5923154900:AAECR2DEtm_zLqnNzRsXy5Wzjm83RqYizDc'

bot: Bot=Bot(bot_token)
dp: Dispatcher=Dispatcher()

attempts: int=5
users: dict={}

@dp.message(Command(commands=['start']))
async def process_start_command(message:Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Что бы получить правила игры и список доступных '
                         'команд - отправьте команду /help')
    if message.from_user.id not in users:
        users[message.from_user.id]={'in_game': False,
                                     'secret_number' : None,
                                     'attempts' : None,  #попытки
                                     'total_games': 0,
                                     'wins':0
                                     }

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {attempts} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')

# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {users[message.from_user.id]["total_games"]}\n'
                         f'Игр выиграно: {users[message.from_user.id]["wins"]}')

@dp.message(Command(commands=['cansel']))
async def procces_stat_command(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть'
                             'снова - напишите об этом')
        users[message.from_user.id]['in-game']=False
    else:
        await message.answer('А мы и так с вами играем. '
                             'Моет сыграем разок?')

@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть', 'Хочу'], ignore_case=True))
async def process_positive_answer(message:Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадай')
        users[message.from_user.id]['in_game']=True
        users[message.from_user.id]['secret_number']=get_random_number()
        users[message.from_user.id]['attempts']=attempts
    else:
        await message.answer('Пока мы играем в игру, я могу '
                              'реагировать только на числа от 1 до 100 '
                               'и команды /cancel и /stat')

@dp.message(Text(text=['Нет', 'Не',  'Не хочу', 'Не буду'], ignore_case=True))
async def process_negative_answer(message:Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Жаль:(\n\nЕсли захотите сыграть - просто '
                             'напиши об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте'
                             'пожалуйста числа от 1 до 100')

@dp.message(lambda x: x.text and x.text.isdigit() and 1<= int(x.text) <=100)
async def process_numbers_answer(message:Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text)==users[message.from_user.id]['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            users[message.from_user.id]['in_game']=False
            users[message.from_user.id]['total_games']+=1
            users[message.from_user.id]['wins']+=1
        elif int(message.text)>users[message.from_user.id]['secret_number']:
            await message.answer('Мое число меньше')
            users[message.from_user.id][attempts]-=1
        elif int(message.text)<users[message.from_user.id]['secret_number']:
            await message.answer('Мое число больше')
            users[message.from_user.id]['attempts']-=1

        if users[message.from_user.id]['attempts']==0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                               f'попыток. Вы проиграли: \n\nМое число '
                               f'было {users[message.from_user.id]["secret_number"]}\n\nДавайте '
                               f'сыграем еще?')
            users[message.from_user.id]['in_game']=False
            users[message.from_user.id]['total_games']+=1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')

@dp.message()
async def process_other_text_answer(message:Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('Мы сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру')

if __name__=='__main__':
    dp.run_polling(bot)







