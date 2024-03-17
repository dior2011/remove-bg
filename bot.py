import asyncio
import logging
import sys 
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery,FSInputFile
from mybuttons import inline_menu,courses_menu,ortga,colours_inline_button,ortga_umumiy
from myremovebg import bg_change_color
TOKEN = "6232855682:AAG-6BbtpsJND2WkXXGjG-UjgHNNvgU4WfY"
dp = Dispatcher()



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum, foto yuboring", reply_markup=inline_menu)
    await message.delete()


@dp.callback_query(F.data == "courses")
async def kurslar(callback:CallbackQuery):
    await callback.message.answer(text="Bizning kurslar", reply_markup=courses_menu)
    await callback.message.delete()


@dp.callback_query(F.data == "frontend")
async def frontend_course(callback:CallbackQuery):   
    image = FSInputFile("C:/Users/Surf_X/Documents/I_Sifat_darslar/telebot/10-dars/remove_bg/front.jpg")
    await callback.message.answer_photo(photo=image, caption="Bizning kurslarimizda siz frontendni o'rganishingiz mumkin!", reply_markup=ortga)
    await callback.message.delete()
    

@dp.callback_query(F.data == "backend")
async def frontend_course(callback:CallbackQuery):   
    image = FSInputFile("C:/Users/Surf_X/Documents/I_Sifat_darslar/telebot/10-dars/remove_bg/front.jpg")
    await callback.message.answer_photo(photo=image, caption="Bizning kurslarimizda siz backendni o'rganishingiz mumkin!", reply_markup=ortga)
    await callback.message.delete()


@dp.callback_query(F.data == "location")
async def frontend_course(callback:CallbackQuery):   
    image = FSInputFile("C:/Users/Surf_X/Documents/I_Sifat_darslar/telebot/10-dars/mavzu/manzil.jpg")
    await callback.message.answer_photo(photo=image, caption="Navoiy viloyati\nNavoiy shahri\nHokimiyat yonida", reply_markup=ortga_umumiy)
    await callback.message.delete()
    

@dp.callback_query(F.data == "back")
async def frontend_course(callback:CallbackQuery):   
    await callback.message.answer(text="Assalomu alaykum, foto yuboring", reply_markup=inline_menu)
    await callback.message.delete()
    
@dp.callback_query(F.data == "back-courses")
async def frontend_course(callback:CallbackQuery):   
    await callback.message.answer(text="Bizning kurslar", reply_markup=courses_menu)
    await callback.message.delete()
    
    
@dp.callback_query(F.data == "about-us")
async def about_us(callback:CallbackQuery):
    await callback.message.answer(text="Yaratuvchi: Xolmurodov Diyorbek", reply_markup=ortga_umumiy)
    await callback.message.delete()
    

@dp.callback_query(F.data == "contact-admin")
async def about_us(callback:CallbackQuery):
    await callback.message.answer_contact(first_name="Diyorbek", phone_number="Xolmurodov", reply_markup=ortga_umumiy)
    await callback.message.delete()  
    
    
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(F.photo)
async def name(message:Message):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"white")
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="start-remove.png"),reply_markup=colours_inline_button)
        # await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-remove.png"))




@dp.callback_query(F.data == "red")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"red")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="red-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


@dp.callback_query(F.data == "black")
async def colours_changes_black(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"black")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="black-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()
    
    
@dp.callback_query(F.data == "brown")
async def colours_changes_brown(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"brown")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="brown-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()
    
    
@dp.callback_query(F.data == "yellow")
async def colours_changes_yellow(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"yellow")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="yellow-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

    
@dp.callback_query(F.data == "blue")
async def colours_changes_blue(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"blue")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="blue-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


@dp.callback_query(F.data == "green")
async def colours_changes_green(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"green")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="green-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()
    
    
@dp.callback_query(F.data == "purple")
async def colours_changes_purple(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"purple")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="purple-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


@dp.callback_query(F.data == "pink")
async def colours_changes_pink(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"pink")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="pink-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


@dp.callback_query(F.data == "back")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"white")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="back-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()





async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



