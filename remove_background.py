import asyncio
import logging
import sys 
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery,FSInputFile
from myremovebg import bg_change_color
TOKEN = "6232855682:AAG-6BbtpsJND2WkXXGjG-UjgHNNvgU4WfY"
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum")


@dp.message(F.photo)
async def bizning_kurslar(message: Message):
    photo_id = message.photo[-1].file_id
    photo = await bot.get_file(photo_id)
    photo_path = photo.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{photo_path}"
    result = dict(bg_change_color(photos_url, 'red'))
    rasm = result.get("image")
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-remove.png"))
    
    
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
