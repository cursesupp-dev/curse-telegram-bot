import asyncio
import os
from datetime import datetime
from telegram import Bot

# Railway Variables (Railway panelden gireceğiz)
BOT_TOKEN = "7950371835:AAFX22AVTFCBimUTA6kTE70lANdM-AnmrEI"
GROUP_ID = -1002520664787

# Mesajlar (saatlik döner)
MESSAGES = [
    "🔥 Curse Supplements 🔥\n👉 https://cursesupp.com",
    "🎁 Kayıt ol, 2500 COIN kazan!\n👉 https://cursesupp.com/account/register",
    "⚡ Telegram’a özel fırsatlar!\n👉 https://cursesupp.com"
]

# Gece susma
QUIET_START = 4   # 04:00
QUIET_END = 8     # 08:00

async def run():
    bot = Bot(token=TOKEN)
    i = 0
    print("🤖 Curse Supplement Bot başladı")

    while True:
        hour = datetime.now().hour

        if QUIET_START <= hour < QUIET_END:
            print("🌙 Sessiz saatler (04:00–08:00)")
        else:
            await bot.send_message(
                chat_id=GROUP_ID,
                text=MESSAGES[i % len(MESSAGES)]
            )
            print("✅ Mesaj gönderildi")
            i += 1

        await asyncio.sleep(3600)  # 1 saat bekle

asyncio.run(run())
