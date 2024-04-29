from aiogram import types, Router,Dispatcher,Bot
import asyncio
from aiogram.filters import Command
import logging
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram import F
import re

PHONE_PATTERN = r"\+998[0-9]{9}" 


logging.basicConfig(level=logging.INFO)
bot = Bot("6703818895:AAGlqielc9bonyjHFXfCIVgmAAB8fEtim4g")
form_router = Router()
dp = Dispatcher()





class IshJoyiKerak(StatesGroup):
    ism = State()
    yosh = State()
    texnologiya = State()
    telefon_raqam = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()


def start_buttons() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="Sherik kerak")
    button_2 = KeyboardButton(text="Ish joyi kerak")
    button_3 = KeyboardButton(text="Xodim kerak")
    button_4 = KeyboardButton(text="Ustoz kerak")
    button_5 = KeyboardButton(text="Shogird  kerak")

    reply_buttons = ReplyKeyboardMarkup(
        keyboard=[
            [button_1,button_2],
            [button_3,button_4],
            [button_5]
        ],resize_keyboard = True
    )
    return reply_buttons

def replay_buttons():
    button = [
        [KeyboardButton(text="Ha")],
        [KeyboardButton(text="Yo'q")]
    ]
    return ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)


@form_router.message(Command('start'))
async def get_started(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}",reply_markup=start_buttons())


@form_router.message(F.text == "Ish joyi kerak")
async def ish_joyi_kerak(message: types.Message,state: FSMContext):
    text = """Ish joyi topish uchun ariza berish

    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi

    Ism,familiyangizni kiriting?
    """
    await message.answer(text=text)
    await state.set_state(IshJoyiKerak.ism)

@form_router.message(IshJoyiKerak.ism)
async def set_user_name(message: types.Message,state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 

    Yoshingizni kiriting?
    Masalan, 19

    """
    await message.answer(text)
    await state.set_state(IshJoyiKerak.yosh)



@form_router.message(IshJoyiKerak.yosh)
async def set_user_name(message: types.Message,state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Yosh faqat sonlardan iborat bo'lsin!!!")
    await state.update_data(yosh=message.text)
    text = """📚 Texnologiya:

    Talab qilinadigan texnologiyalarni kiriting?
    Texnologiya nomlarini vergul bilan ajrating. Masalan, 

    Java, C++, C#
    """ 
    await message.answer(text)
    await state.set_state(IshJoyiKerak.texnologiya)

@form_router.message(IshJoyiKerak.texnologiya)
async def state_user_name(message: types.Message,state: FSMContext):
    await state.update_data(texnologiya=message.text)
    text = """📞 Aloqa: 

    Bog`lanish uchun raqamingizni kiriting?
    Masalan, +998 90 123 45 67
    """
    await message.answer(text)
    await state.set_state(IshJoyiKerak.telefon_raqam)


@form_router.message(IshJoyiKerak.telefon_raqam)
async def state_user_name(message: types.Message,state: FSMContext):
    if not re.match(PHONE_PATTERN,message.text):
        return await message.answer("Uzbekiston raqami bo'lishiga ishonch hosil qiling!!!")
    await state.update_data(telefon_raqam=message.text)
    text = """🌐 Hudud: 

    Qaysi hududdansiz?
    Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
    """
    await message.answer(text)
    await state.set_state(IshJoyiKerak.hudud)

@form_router.message(IshJoyiKerak.hudud)
async def state_user_name(message: types.Message,state: FSMContext):
    await state.update_data(hudud=message.text)
    text = """💰 Narxi:

    Tolov qilasizmi yoki Tekinmi?
    Kerak bo`lsa, Summani kiriting?.
    """
    await message.answer(text)
    await state.set_state(IshJoyiKerak.narx)

@form_router.message(IshJoyiKerak.narx)
async def state_user_name(message: types.Message,state: FSMContext):
    await state.update_data(narx=message.text)
    text = """👨🏻‍💻 Kasbi: 

    Ishlaysizmi yoki o`qiysizmi?
    Masalan, Talaba
    """
    await message.answer(text)
    await state.set_state(IshJoyiKerak.kasb)


@form_router.message(IshJoyiKerak.kasb)
async def state_user_name(message: types.Message,state: FSMContext):
    await state.update_data(kasb=message.text)
    text = """🕰 Murojaat qilish vaqti: 

    Qaysi vaqtda murojaat qilish mumkin?
    Masalan, 9:00 - 18:00
    """
    await message.answer(text)
    await state.set_state(IshJoyiKerak.vaqt)


@form_router.message(IshJoyiKerak.vaqt)
async def state_user_name(message: types.Message,state: FSMContext):
    await state.update_data(vaqt=message.text)
    text = """🔎 Maqsad: 

    Maqsadingizni qisqacha yozib bering.
    """
    await message.answer(text)
    await state.set_state(IshJoyiKerak.maqsad)

@form_router.message(IshJoyiKerak.maqsad, F.text == 'Ha')
async def send_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = f"""Ish joyi kerak:

    👨‍💼 Xodim: {message.from_user.full_name}
    🕑 Yosh: {data["yosh"]}
    📚 Texnologiya: {data["texnologiya"]} 
    🇺🇿 Telegram: @{message.from_user.username}
    📞 Aloqa: {data["telefon_raqam"]}
    🌐 Hudud: {data["hudud"]} 
    💰 Narxi: {data["narx"]} 
    👨🏻‍💻 Kasbi: {data["kasb"]}
    🕰 Murojaat qilish vaqti: {data["vaqt"]}
    🔎 Maqsad: {data["maqsad"]}
    """
    await bot.send_message(chat_id=5715413519, text=text)
    await state.clear()

@form_router.message(IshJoyiKerak.maqsad, F.text == 'Yo\'q')
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("Qaytadan to'ldiring")
    await state.clear()

@form_router.message(IshJoyiKerak.maqsad)
async def state_user_name(message: types.Message,state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    text = f"""Ish joyi kerak:

    👨‍💼 Xodim: {message.from_user.full_name}
    🕑 Yosh: {data["yosh"]}
    📚 Texnologiya: {data["texnologiya"]} 
    🇺🇿 Telegram: @{message.from_user.username}
    📞 Aloqa: {data["telefon_raqam"]}
    🌐 Hudud: {data["hudud"]} 
    💰 Narxi: {data["narx"]} 
    👨🏻‍💻 Kasbi: {data["kasb"]}
    🕰 Murojaat qilish vaqti: {data["vaqt"]}
    🔎 Maqsad: {data["maqsad"]}
    """
    await message.answer(text=text)
    await message.answer(text="Ma'lumotlar to'g'rimi ?",reply_markup=replay_buttons())














async def main():
    dp.include_router(form_router)
    await dp.start_polling(bot)

if __name__ =="__main__":
    asyncio.run(main())