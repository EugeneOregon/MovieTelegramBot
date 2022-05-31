from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import channels
from keyboards.inline.callback_datas import choice_callback
from loader import bot, db


# New post with inline button
async def new_post(link):
    channel = channels[0]
    movie = await db.select_film(link=link)
    # Number of buttons
    watch = InlineKeyboardMarkup(row_width=1)
    # Button with link
    watch_movie = InlineKeyboardButton(text="Смотреть", callback_data=choice_callback.new(item_name="watch"),
                                       url=movie['url'])
    watch.insert(watch_movie)
    # Publish post via send_photo method(excludes the visible part of the link in the post)
    await bot.send_photo(chat_id=channel, photo=movie['poster'], caption=movie['title'], reply_markup=watch)
