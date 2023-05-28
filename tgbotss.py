import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = '5863651336:AAHhUJ9Yhgkw5ssijpjlSwqdTPZi40Rtxik'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

inl_menu = InlineKeyboardMarkup(row_width = 2,
                                inline_keyboard = [
                                    [
                                        InlineKeyboardButton(text = '🥃КАНАЛ С СИГНАЛАМИ🥃', url = 'https://t.me/+UHTEdseipL9kMDZi')                   
                                    ],

                                    [
                                        InlineKeyboardButton(text = '✅LUCKYJET✅', url = 'https://1wsref.top/casino/list?open=register')
                                    ]

                                ])

@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    user_id = update.from_user.id
    await bot.send_message(user_id, '<b>Приветствую тебя! 🐻 \nНа связи Ричард 💻</b> \nХочу сказать, что ты красава, только потому, что зашёл ко мне ✅ \nЧто тебя ждёт? \n🔥Ежедневно бесплатные сигналы на игру. \n1) <a href="https://1wsref.top/casino/list?open=register">LuckyJet 1 win</a> 8️⃣ \n❌Наш телеграмм канал👉 <a href="https://1wsref.top/casino/?open=register">тут</a> \n⚠️Информация как бесплатно вступить в наш вип канал👉 <a href="https://telegra.ph/KAK-VSTUPIT-V-VIP-BESPLATNO-03-23">читать</a> \n🔴<b>Жду на стримах</b> ❤️🔥✅', reply_markup = inl_menu, parse_mode=types.ParseMode.HTML)
    

    await update.approve() 


if __name__ == '__main__':
    executor.start_polling(dp)

    #Приветствую тебя! \xF0\x9F\x90\xBB \nНа связи Ричард  \xF0\x9F\x92\xBB \nХочу сказать, что ты красава, только потому, что зашёл ко мне \xE2\x9C\x85 \nЧто тебя ждёт? \n\xF0\x9F\x94\xA5Ежедневно бесплатные сигналы на игру. \n1) LuckyJet 1 win (https://1wsref.top/casino/list?open=register)\xE2\xAD\x95 \n\xE2\x9D\x8CНаш телеграмм канал\xF0\x9F\x91\x89 f{text} \n\xE2\x9A\xA0Информация как бесплатно вступить в наш вип канал\xF0\x9F\x91\x89 f{text1} \n\xE2\xAD\x95Жду на стримах \xF0\x9F\x92\x93\xF0\x9F\x94\xA5\xE2\x9C\x85