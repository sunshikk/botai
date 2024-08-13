import g4f
import asyncio

from aiogram import F, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from settings.settings import ai_token

import files.keyboards as kb
from files import database as db

# class Form(StatesGroup):

router = Router()

@router.message(StateFilter(None), CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    db.cur.execute("INSERT OR IGNORE INTO users (user_id, limit_request, lang) VALUES (?, ?, ?)", (user_id, 5, None))
    db.db.commit()
    await message.answer("👋 Привет!\nНажмите на соответствующую кнопку для продолжения\n\nДля получения дополнительной помощи, нажмите '❓ Помощь'", reply_markup=kb.start)


@router.callback_query() 
async def process_callback(callback_query: CallbackQuery, state: FSMContext): 
    data = callback_query.data

    if data == "learnlang":
        await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        await callback_query.message.answer("📕 Выберите язык, по которому вы хотите получить задание.", reply_markup=kb.learn)

    if data == "ret":
        await callback_query.message.answer("👋 Привет!\nНажмите на соответствующую кнопку для продолжения\n\nДля получения дополнительной помощи, нажмите '❓ Помощь'", reply_markup=kb.start)

    if data == "py":
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.3,
            # max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None,
            messages=[
                {"role": "user", "content": (
                    "Привет ChatGPT! Дай пожалуйста мне среднюю, не сложную задачу по языке программирования Python и дай совет по решению этой задачи.",
                    "Ты всегда выдаешь разные задачи",
                    "Ты используешь русский язык в своем ответе.",
                    "Ты используешь смайлики в своем ответе.",
                    "Ты обязательно даешь код для решения задачи, которую ты задал пользователю.",
                    "Ты обязательно поясняешь код задачи пользователю.",
                    "Ты всегда говоришь в конце: Если тебе нужны еще задачи, дай мне об этом знать!")
                }
            ],
            stream=True
        )
        language = db.cur.execute("SELECT lang FROM users WHERE user_id = {}".format(callback_query.from_user.id)).fetchone()[0]
        if language == None:
            await callback_query.bot.edit_message_text(
                text="✅ Вы успешно выбрали язык <b>🐍 Python</b> как основной\n\nНажмите 'Назад', чтобы вернуться в меню.",
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb.inlearn
            )
            db.cur.execute("UPDATE users SET lang = ? WHERE user_id = ?", ("Python", callback_query.from_user.id))
            db.db.commit()
        else:
            await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id,message_id=callback_query.message.message_id)
            await callback_query.message.answer("Ваша задача генерируется, пожалуйста, подождите...")
            response_text = ""
            for chunk in response:
                response_text += chunk
                await asyncio.sleep(3)
                await callback_query.message.answer(response_text, parse_mode="Markdown", reply_markup=kb.inlearn)
                return

    if data == "js":
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.3,
            # max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None,
            messages=[
                {"role": "user", "content": (
                    "Привет ChatGPT! Дай пожалуйста мне среднюю, не сложную задачу по языке программирования JavaScript и дай совет по решению этой задачи.",
                    "Ты всегда выдаешь разные задачи",
                    "Ты используешь русский язык в своем ответе.",
                    "Ты используешь смайлики в своем ответе.",
                    "Ты обязательно даешь код для решения задачи, которую ты задал пользователю.",
                    "Ты обязательно поясняешь код задачи пользователю.",
                    "Ты всегда говоришь в конце: Если тебе нужны еще задачи, дай мне об этом знать!")
                }
            ],
            stream=True
        )
        language = db.cur.execute("SELECT lang FROM users WHERE user_id = {}".format(callback_query.from_user.id)).fetchone()[0]
        if language == None:
            await callback_query.bot.edit_message_text(
                text="✅ Вы успешно выбрали язык <b>🟨 JavaScript</b> как основной\n\nНажмите 'Назад', чтобы вернуться в меню.",
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb.inlearn
            )
            db.cur.execute("UPDATE users SET lang = ? WHERE user_id = ?", ("JavaScript", callback_query.from_user.id))
            db.db.commit()
        else:
            await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id,message_id=callback_query.message.message_id)
            await callback_query.message.answer("Ваша задача генерируется, пожалуйста, подождите...")
            response_text = ""
            for chunk in response:
                response_text += chunk
                await asyncio.sleep(3)
                await callback_query.message.answer(response_text, parse_mode="Markdown", reply_markup=kb.inlearn)
                return

    if data == "java":
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.3,
            # max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None,
            messages=[
                {"role": "user", "content": (
                    "Привет ChatGPT! Дай пожалуйста мне среднюю, не сложную задачу по языке программирования Java и дай совет по решению этой задачи.",
                    "Ты всегда выдаешь разные задачи",
                    "Ты используешь русский язык в своем ответе.",
                    "Ты используешь смайлики в своем ответе.",
                    "Ты обязательно даешь код для решения задачи, которую ты задал пользователю.",
                    "Ты обязательно поясняешь код задачи пользователю.",
                    "Ты всегда говоришь в конце: Если тебе нужны еще задачи, дай мне об этом знать!")
                }
            ],
            stream=True
        )
        language = db.cur.execute("SELECT lang FROM users WHERE user_id = {}".format(callback_query.from_user.id)).fetchone()[0]
        if language == None:
            await callback_query.bot.edit_message_text(
                text="✅ Вы успешно выбрали язык <b>☕ Java</b> как основной\n\nНажмите 'Назад', чтобы вернуться в меню.",
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb.inlearn
            )
            db.cur.execute("UPDATE users SET lang = ? WHERE user_id = ?", ("Java", callback_query.from_user.id))
            db.db.commit()
        else:
            await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id,message_id=callback_query.message.message_id)
            await callback_query.message.answer("Ваша задача генерируется, пожалуйста, подождите...")
            response_text = ""
            for chunk in response:
                response_text += chunk
                await asyncio.sleep(3)
                await callback_query.message.answer(response_text, parse_mode="Markdown", reply_markup=kb.inlearn)
                return

    if data == "cs":
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.3,
            # max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None,
            messages=[
                {"role": "user", "content": (
                    "Привет ChatGPT! Дай пожалуйста мне среднюю, не сложную задачу по языке программирования C# и дай совет по решению этой задачи.",
                    "Ты всегда выдаешь разные задачи",
                    "Ты используешь русский язык в своем ответе.",
                    "Ты используешь смайлики в своем ответе.",
                    "Ты обязательно даешь код для решения задачи, которую ты задал пользователю.",
                    "Ты обязательно поясняешь код задачи пользователю.",
                    "Ты всегда говоришь в конце: Если тебе нужны еще задачи, дай мне об этом знать!")
                }
            ],
            stream=True
        )
        language = db.cur.execute("SELECT lang FROM users WHERE user_id = {}".format(callback_query.from_user.id)).fetchone()[0]
        if language == None:
            await callback_query.bot.edit_message_text(
                text="✅ Вы успешно выбрали язык <b>#️⃣ C#</b> как основной\n\nНажмите 'Назад', чтобы вернуться в меню.",
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb.inlearn
            )
            db.cur.execute("UPDATE users SET lang = ? WHERE user_id = ?", ("C#", callback_query.from_user.id))
            db.db.commit()
        else:
            await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id,message_id=callback_query.message.message_id)
            await callback_query.message.answer("Ваша задача генерируется, пожалуйста, подождите...")
            response_text = ""
            for chunk in response:
                response_text += chunk
                await asyncio.sleep(3)
                await callback_query.message.answer(response_text, parse_mode="Markdown", reply_markup=kb.inlearn)
                return

    if data == "cpp":
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.3,
            # max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None,
            messages=[
                {"role": "user", "content": (
                    "Привет ChatGPT! Дай пожалуйста мне среднюю, не сложную задачу по языке программирования C++ и дай совет по решению этой задачи.",
                    "Ты всегда выдаешь разные задачи",
                    "Ты используешь русский язык в своем ответе.",
                    "Ты используешь смайлики в своем ответе.",
                    "Ты обязательно даешь код для решения задачи, которую ты задал пользователю.",
                    "Ты обязательно поясняешь код задачи пользователю.",
                    "Ты всегда говоришь в конце: Если тебе нужны еще задачи, дай мне об этом знать!")
                }
            ],
            stream=True
        )
        language = db.cur.execute("SELECT lang FROM users WHERE user_id = {}".format(callback_query.from_user.id)).fetchone()[0]
        if language == None:
            await callback_query.bot.edit_message_text(
                text="✅ Вы успешно выбрали язык <b>➕ C++</b> как основной\n\nНажмите 'Назад', чтобы вернуться в меню.",
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb.inlearn
            )
            db.cur.execute("UPDATE users SET lang = ? WHERE user_id = ?", ("C++", callback_query.from_user.id))
            db.db.commit()
        else:
            await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id,message_id=callback_query.message.message_id)
            await callback_query.message.answer("Ваша задача генерируется, пожалуйста, подождите...")
            response_text = ""
            for chunk in response:
                response_text += chunk
                await asyncio.sleep(3)
                await callback_query.message.answer(response_text, parse_mode="Markdown", reply_markup=kb.inlearn)
                return