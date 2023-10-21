
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from Mahmoudquran import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="◈ اغلاق ◈", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
    ],
    [
            InlineKeyboardButton(text=" II ", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="◈ اضفني لمجموعتك ◈",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="◈ الاوامر ◈", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="", url="https://t.me/VL_VD"
        ),
        InlineKeyboardButton(text="◈ مالك البوت ◈", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="◈ اضفني لمجموعتك ◈",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="◈ السورس ◈", url=config.SUPPORT_CHANNEL),
     
        InlineKeyboardButton(text="", url=config.SUPPORT_CHAT),
 
        InlineKeyboardButton(
            text="◈ المطور ◈", url="https://t.me/VL_VD"
        ),
        InlineKeyboardButton(text="", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="◈ الاوامر ◈",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="◈ اوامࢪ المطور ◈", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="◈ اوامر المالك ◈", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="◈ عودة ◈", callback_data="fallen_home"),
        InlineKeyboardButton(text="◈ اغلاق ◈", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="◈ السورس ◈", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="◈ عودة ◈", callback_data="fallen_help"),
        InlineKeyboardButton(text="◈ اغلاق ◈", callback_data="close"),
    ],
]
