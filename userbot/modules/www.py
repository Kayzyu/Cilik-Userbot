# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
import redis

from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register

absen = [
    "**Hadir ganteng** ð¥µ",
    "**Hadir bro** ð",
    "**Hadir kak** ð",
    "**Hadir bang** ð",
    "**Hadir kak maap telat** ð¥º",
    "**Hadir Bang Grey**",
    "**Hadir Sayang** ð¥µ"
    "**Hadir Bang Grey** ð",
    "**Hadir Beb** ð ",
    "**Hadir Bang Grey** ð",
    "**Hadir Grey Pacar Aku**",
    "**Halo Grey**",
]

pacar = [
    "**Kamu mau jadi pacar aku ga?** ð",
    "**Memek mending sama aku** ð",
    "**Hai ganteng** ð·",
    "**Mau ga bang jadi pacar aku?** ð",
    "**Mending pc aku bang** ð¥º",
    "**Ngewe Sama Aku yuk**ð¥µð¥µð¦",
    "**Grey Mau Aku Crotin??**ð¥µ",
    "**Grey Mau Aku Sepongin??**",
    "**Grey Aku Sayang Kamu ,Mwahhhð**",
]

salam = [
    "**Wa'alaikumsalam ganteng** ð¥°ð¥°",
    "**Wa'alaikumsalam WR WB** ðð»",
    "**Iyah Waalaikusalam** ð¥µ",
    "**Wa'alaikumsalam bang**",
    "**Wa'alaikumsalam** ð¥°",
    "**Wa'alaikumsalan Warohmatullohi Wabarokatu**",
    "**Wa'alaikumsalam Ustad**",
]
    

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=1784606556, pattern=r"^.absen$")
async def _(grey):
    await grey.reply(random.choice(absen))


@register(incoming=True, from_users=1784606556, pattern=r"^.grey$")
async def _(grey):
    await grey.reply(random.choice(pacar))
    
    
@register(incoming=True, from_users=1784606556, pattern=r"^.p$")
async def _(grey):
    await grey.reply(random.choice(salam))
    

@register(outgoing=True, pattern="^.sping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**â²**")
    await pong.edit("**â²â²**")
    await pong.edit("**â²â²â²**")
    await pong.edit("__DUAR__")
    await pong.edit("ð¥")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**{ALIVE_NAME}**        \n"
        f"**â¾Kecepatan : ** '%sms'  \n"
        f"**â¾Branch : ** 'Cilik-Userbot` \n" % (duration)
    )


@register(outgoing=True, pattern="^.lping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**`{ALIVE_NAME}`**\n"
        f"â§ **-ê±ÉªÉ¢É´á´Ê- :** "
        f"`%sms` \n"
        f"â§ **-á´á´á´Éªá´á´- :** "
        f"`{uptime}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**â¨Cilik-Userbotâ¨**\n"
        f"â¾ __Signal__    __:__ "
        f"`%sms` \n"
        f"â¾ __Uptime__ __:__ "
        f"`{uptime}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.sinyal$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Mengecek Sinyal...**")
    await pong.edit("**0% ââââââââââ**")
    await pong.edit("**20% ââââââââââ**")
    await pong.edit("**40% ââââââââââ**")
    await pong.edit("**60% ââââââââââ**")
    await pong.edit("**80% ââââââââââ**")
    await pong.edit("**100% ââââââââââ**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**â¨ Cilik-Userbot â¨**\n\n"
        f"** â¹  SÉªÉ¢É´á´Ê   :** "
        f"`%sms` \n"
        f"** â¹  Uá´á´Éªá´á´  :** "
        f"`{uptime}` \n"
        f"** â¹  Oá´¡É´á´Ê   :** `{ALIVE_NAME}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**â«**")
    await pong.edit("**â«â«**")
    await pong.edit("**â«â«â«**")
    await pong.edit("**â«â«â«â«**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**PONG!!ð**\n"
        f"â£ **Pinger** - `%sms`\n"
        f"â£ **Uptime -** `{uptime}` \n"
        f"**â¦ÒÍ¡ÍOwner :** `{ALIVE_NAME}`" % (duration)
    )


@register(outgoing=True, pattern="^.kecepatan$")
async def speedtst(spd):
    """For .speed command, use SpeedTest to check server speeds."""
    await spd.edit("**Sedang Menjalankan Tes Kecepatan Jaringan,Mohon Tunggu...**")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(
        "**Kecepatan Jaringan:\n**"
        " âââââââââââââââââ \n"
        f"â§ **Dimulai Pada :**  \n"
        f"`{result['timestamp']}` \n"
        "â§ **Download:** "
        f"`{speed_convert(result['download'])}` \n"
        "â§ **Upload:** "
        f"`{speed_convert(result['upload'])}` \n"
        "â§ **Signal:** "
        f"`{result['ping']}` \n"
        "â§ **ISP:** "
        f"`{result['client']['isp']}` \n"
        "â§ **BOT:** â¨Cilik-Userbotâ¨"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    await pong.edit("**ââ¿- PONG!!ð**")
    await asyncio.sleep(1)
    await pong.edit("â¨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**â¨KyyName : {ALIVE_NAME}**\nð `%sms`" % (duration))


@register(outgoing=True, pattern="^.pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8â===D")
    await pong.edit("8=â==D")
    await pong.edit("8==â=D")
    await pong.edit("8===âD")
    await pong.edit("8==â=D")
    await pong.edit("8=â==D")
    await pong.edit("8â===D")
    await pong.edit("8=â==D")
    await pong.edit("8==â=D")
    await pong.edit("8===âD")
    await pong.edit("8==â=D")
    await pong.edit("8=â==D")
    await pong.edit("8â===D")
    await pong.edit("8=â==D")
    await pong.edit("8==â=D")
    await pong.edit("8===âD")
    await pong.edit("8===âDð¦")
    await pong.edit("8====Dð¦ð¦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**BABI!! **\n**NGENTOT** : %sms\n**Bot Uptime** : {uptime}ð" % (duration)
    )


CMD_HELP.update(
    {
        "ping": "ð¾ð¤ð¢ð¢ðð£ð: `.ping` | `.lping` | `.xping` | `.sinyal` | `.sping` | `.pink`\
         \nâ³ : Untuk Menunjukkan Ping Bot Anda.\
         \n\nð¾ð¤ð¢ð¢ðð£ð: `.kecepatan`\
         \nâ³ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\nð¾ð¤ð¢ð¢ðð£ð: `.pong`\
         \nâ³ : Sama Seperti Perintah Ping."
    }
)
