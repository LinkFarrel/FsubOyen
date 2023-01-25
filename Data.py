# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

👨‍💻 Develoved by </b><a href='https://t.me/kunapya'>@kunapya</a>
"""

    close = [
        [InlineKeyboardButton("•𝐓𝐔𝐓𝐔𝐏•", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("•𝐇𝐄𝐋𝐏 & 𝐏𝐄𝐑𝐈𝐍𝐓𝐀𝐇•", callback_data="help"),
            InlineKeyboardButton("•𝐓𝐔𝐓𝐔𝐏•", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("•𝐓𝐄𝐍𝐓𝐀𝐍𝐆 𝐁𝐎𝐓 𝐈𝐍𝐈•", callback_data="about"),
            InlineKeyboardButton("•𝐓𝐔𝐓𝐔𝐏•", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://github.com/LinkFarrel/FsubOyen'>ForceSubsOyen</a>

👨‍💻 Develoved by </b><a href='https://t.me/kunapya'>@kunapya</a>
"""
