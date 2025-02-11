# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="•𝐇𝐄𝐋𝐏 & 𝐏𝐄𝐑𝐈𝐍𝐓𝐀𝐇•", callback_data="help"),
                InlineKeyboardButton(text="•𝐓𝐔𝐓𝐔𝐏•", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="•𝐆𝐑𝐎𝐔𝐏•", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="•𝐇𝐄𝐋𝐏 & 𝐏𝐄𝐑𝐈𝐍𝐓𝐀𝐇•", callback_data="help"),
                InlineKeyboardButton(text="•𝐓𝐔𝐓𝐔𝐏•", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="•𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="•𝐇𝐄𝐋𝐏 & 𝐏𝐄𝐑𝐈𝐍𝐓𝐀𝐇•", callback_data="help"),
                InlineKeyboardButton(text="•𝐓𝐔𝐓𝐔𝐏•", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="•𝐇𝐄𝐋𝐏 & 𝐏𝐄𝐑𝐈𝐍𝐓𝐀𝐇•", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="•𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", url=client.invitelink),
                InlineKeyboardButton(text="•𝐆𝐑𝐎𝐔𝐏•", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="•𝐓𝐔𝐓𝐔𝐏•", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="•𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏•", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="•𝐂𝐎𝐁𝐀 𝐔𝐋𝐀𝐍𝐆•",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="•𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="•𝐂𝐎𝐁𝐀 𝐋𝐀𝐆𝐈•",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="•𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", url=client.invitelink),
                InlineKeyboardButton(text="•𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏•", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="•𝐂𝐎𝐁𝐀 𝐔𝐋𝐀𝐍𝐆•",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
