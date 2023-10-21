

from pyrogram import filters
from pyrogram.types import Message

from Mahmoudquran import SUDOERS, app
from Mahmoudquran.Helpers.active import get_active_chats
from Mahmoudquran.Helpers.inline import close_key


@app.on_message(filters.command("activevc") | filters.command(["المكالمات","النشطه"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("⌔︙ جاري جلب المكالمات ⚡")
    chats = await get_active_chats()
    text = ""
    j = 0
    for chat in chats:
        try:
            title = (await app.get_chat(chat)).title
        except Exception:
            title = "جـروب خـاص"
        if (await app.get_chat(chat)).username:
            user = (await app.get_chat(chat)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("⌔︙ لا يـوجد مكالمات في الوقت الحالي")
    else:
        await mystic.edit_text(
            f"**قائمة المكالمات الشغالة :**\n\n{text}",
            reply_markup=close_key,
            disable_web_page_preview=True,
        )
