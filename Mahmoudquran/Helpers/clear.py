

from Mahmoudquran import fallendb
from Mahmoudquran.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        fallendb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
