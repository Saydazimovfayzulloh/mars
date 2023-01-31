from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuMain = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text="Mahsulotlar"),
            
            KeyboardButton(text="Qollanma")
        ],
        
    ],
    resize_keyboard=True
)


menuBack = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Orqaga')
        ]
    ],
    resize_keyboard=True
)