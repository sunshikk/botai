from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
 
learn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🐍 Python", callback_data="py")],[InlineKeyboardButton(text="🟨 JavaScript", callback_data="js")],
    [InlineKeyboardButton(text="☕ Java", callback_data="java")],[InlineKeyboardButton(text="#️⃣ C#", callback_data="cs")],
    [InlineKeyboardButton(text="➕ C++", callback_data="cpp")]
])

inlearn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад", callback_data="ret")]
])

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📕 Выучить язык", callback_data="learnlang")]
])