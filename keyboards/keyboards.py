from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Кнопка один')],
        [KeyboardButton(text='Кнопка два')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Доминируйте...'
)

someKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Кнопка инлайн 1', callback_data='button1')],
        [InlineKeyboardButton(text='Кнопка инлайн 2', callback_data='button2')]
    ]
)