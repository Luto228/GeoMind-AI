import asyncio
import aiohttp

from config import TOKEN

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

bot = Bot(token = TOKEN)
dispatcher = Dispatcher()

@dispatcher.message(CommandStart())
async def StartCommand(message: types.Message):
    await message.answer(f'Hi!\nThis is a bot where you can enter any city and the bot will return:\n1. Country\n2. Population\n3. Weather \nenter: /info [country]')

@dispatcher.message(Command('info'))
async def InfoCountry(message: Message):
    messageSize = message.text.split()
    messageIndex = len(messageSize)
    if messageIndex != 2:
        await message.answer(f'Inccorect! \nEnter: /info [country]')
    else:
        await message.answer(f'i use all my 3000IQ to find...')
        country = messageSize[1]
        url = f"https://restcountries.com/v3.1/name/{country}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    info = data[0]
                    name = f"{info['name']['common']} {info['flag']}"
                    population = info['population']
                    capital = info['capital'][0]
                    await message.answer(f'everything is found! \nName: {name}, \npopulation: {population}, \ncapital: {capital}')
                elif response.status == 404:
                    await message.answer(f'I couldn\'t find country!')

async def main():
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')