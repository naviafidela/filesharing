from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import asyncio
import random
import aiohttp
from io import BytesIO
from PIL import Image
import ntplib, time, os
from pyrogram.enums import ParseMode

from bot import Bot

# === Event: User Baru Masuk Grup ===
@Bot.on_message(filters.new_chat_members)
async def add_group(client, message):
    for member in message.new_chat_members:
        name = member.first_name
        if member.last_name:
            name += " " + member.last_name

        share_message = (
            "🔥𝗕𝗘𝗥𝗚𝗔𝗕𝗨𝗡𝗚 𝗗𝗜 𝗚𝗥𝗨𝗣 𝗕𝗔𝗥𝗨🔥\n\n"
            "⭐ 𝙋𝙀𝙈𝙀𝙍𝙎𝘼𝙏𝙐 𝘽𝘼𝙉𝙂𝙎𝘼 💦/n"
            "➤ __https://t.me/VideoAsupanViralBot?start=Z2V0LTMzMDY4MTU0MzI0Mjgy__\n\n"
            "⭐ 𝘼𝙎𝙐𝙋𝘼𝙉 𝙎𝙈𝘼 💦\n"
            "➤ __https://t.me/joinchat/JdpYxovFx3IyMjg1__\n\n"
            "⭐ 𝘽𝙊𝙆𝙀𝙋𝙎𝙀𝙉𝙅𝘼 💦\n"
            "➤ __https://t.me/joinchat/j4cRH_jg7VJhN2I1__"
        )

        from urllib.parse import quote
        encoded_message = quote(share_message)

        keyboard = [
            [
                InlineKeyboardButton("🔐 ʙᴜᴋᴀ ᴋᴜɴᴄɪ ᴍᴇᴅɪᴀ 🔐", url=f"tg://msg?text={encoded_message}")
            ],
            [
                InlineKeyboardButton("✨ᴀꜱᴜᴘᴀɴ ᴠɪʀᴀʟ✨", url="https://t.me/VideoAsupanViralBot?start=Z2V0LTMzMDY4MTU0MzI0Mjgy"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        sent_message = await client.send_photo(
            chat_id=message.chat.id,
            photo="https://i.ibb.co/L8YvcTB/6276011250815189839-120.jpg",
            parse_mode=ParseMode.HTML,
            caption=f"👋 Hai {name}\n\n"
                    "Semua Chat Disembunyikan Untuk Anggota Baru\n"
                    "Anda Harus Membuka Kunci Dengan Cara Bagikan Ke 3 - 5 Grup.\n\n"
                    "Total Media Grup :\n"
                    "📷 Foto = 75683\n"
                    "📹 Video = 27603\n\n"
                    "Cara Buka Kunci Media:\n"
                    "Klik Tombol Buka Kunci Dan Bagikan Ke 3 - 5 Grup Untuk Membuka.\n\n"
                    "Note:\n"
                    "Jika Terverifikasi Anda Sudah Bisa Mengirim Pesan Dan Melihat Video Di Grup Ini.\n",
            reply_markup=reply_markup,
            has_spoiler=True
        )

        await asyncio.sleep(120)
        await sent_message.delete()
