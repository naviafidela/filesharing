from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import asyncio
import random
import aiohttp
from io import BytesIO
from PIL import Image
import ntplib, time, os

from bot import Bot

# === Event: User Baru Masuk Grup ===
@Bot.on_message(filters.new_chat_members)
async def add_group(client, message):
    for member in message.new_chat_members:
        name = member.first_name
        if member.last_name:
            name += " " + member.last_name

        share_message = (
            "🔥 **Bergabung di Grup Baru :**\n\n"
            "**BokepSenja .com** 💦 : https://t.me/joinchat/j4cRH_jg7VJhN2I1\n\n"
            "**Asupan SMA** 💦 : https://t.me/joinchat/JdpYxovFx3IyMjg1\n\n"
            "**Channel ** 💦 : @BokepSenjaBot\n\n"
            "**Website** : https://bokepsenja.com"
        )

        from urllib.parse import quote
        encoded_message = quote(share_message)

        keyboard = [
            [InlineKeyboardButton("🔐 Buka Kunci Media 🔐", url=f"tg://msg?text={encoded_message}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        sent_message = await client.send_photo(
            chat_id=message.chat.id,
            photo="https://i.ibb.co/L8YvcTB/6276011250815189839-120.jpg",
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

        await asyncio.sleep(30)
        await sent_message.delete()
