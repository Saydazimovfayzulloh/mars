from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

meneProducts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="Kitoblar", callback_data="books")
        ],
        [
            InlineKeyboardButton(text="YouTube Sahifamiz", url="https://www.youtube.com/@marsitschool7823"),
        ],
        [
            InlineKeyboardButton(text="Ulashiz", switch_inline_query="Bu foydali bot ekan" ),
        ],
    ]
)

meneCourses = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python Dasturlash Tili", callback_data="python"),
            InlineKeyboardButton(text="Dizayn", callback_data="dizayn")
        ]
    ]
)