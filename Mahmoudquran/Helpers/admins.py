

from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

from Mahmoudquran import SUDOERS, app

from .active import is_active_chat


def admin_check(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if not await is_active_chat(message.chat.id):
            return await message.reply_text("لا يتم تشغيل البوت عبر دردشة الفيديو.")

        if message.from_user.id in SUDOERS:
            return await func(_, message)

        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "⌔︙ انـت لـسـت ادمـن اکـعـد و انـجـب لـتـلـعـب"
            )

        admin = (
            await app.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, message)
        else:
            return await message.reply_text(
                "⌔︙ ليس لديك أذونات لإدارة محادثات الفيديو "
            )

    return non_admin


def admin_check_cb(func: Callable) -> Callable:
    async def cb_non_admin(_, query: CallbackQuery):
        if not await is_active_chat(query.message.chat.id):
            return await query.answer(
                "الـبـوت لا يـبـث فـي الـمـحـادثـة الـصـوتـيـة", show_alert=True
            )

        if query.from_user.id in SUDOERS:
            return await func(_, query)

        try:
            check = await app.get_chat_member(query.message.chat.id, query.from_user.id)
        except:
            return
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await query.answer(
                "⌔︙ انـت لـسـت مـشـرف اکـعـد و انـجـب لـتـلـعـب ",
                show_alert=True,
            )

        admin = (
            await app.get_chat_member(query.message.chat.id, query.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, query)
        else:
            return await query.answer(
                "⌔︙ ليس لديك أذونات لإدارة محادثات الفيديو",
                show_alert=True,
            )

    return cb_non_admin
