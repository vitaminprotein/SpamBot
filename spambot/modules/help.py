import asyncio
from hackingaibot import gladiator, StartTime, OWNER_ID, OWNER_NAME, REPO_NAME, SUDO_USERS, DEV_USERS
from telethon import events, custom, Button
from datetime import datetime
import time


def get_uptime(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    uptime_ret = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if uptime_ret.endswith(":"):
        return uptime_ret[:-1]
    else:
        return uptime_ret

DEFAULTUSER = str(OWNER_NAME)
help_img = "https://telegra.ph/file/6e92103071aa47ee7023e.mp4"

dev_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**


**/ping:** Check ping of the server.
**/logs:** Get logs of your heroku app.
**/usage:** Check usage of your heroku app.
**/restart:** Restarts the bot.(Too fast!! **Supersonic**)

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @Gladiators_Projects
"""
spam_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

**/spam:** Spams text for given counter!!\nSyntax: /spam <counter> <text>
**/uspam:** Spams text continuosly!!\nSyntax: /uspam <text>
**/dspam:** Delay spam a text for given counter after given time!!
Syntax: /dspam <seconds> <counter> <text>
**/wspam:** Spams words in a message!!\nSyntax: /wspam <text>
**/mspam:** Spams media for given counter!!
Syntax: /mspam <counter>
(replying to any media)
**/packspam:** Spams all stickers from sticker pack!!
Syntax: /packspam (replying to any sticker)
**/hang:** Spams hanging message for given counter!!
Syntax: /hang <counter>

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @Gladiators_Projects
"""
start_img = "https://telegra.ph/file/1312f063f0395fc933edd.mp4"

help_caption = """
**Hᴇʏ ᴍᴀsᴛᴇʀ,
ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜᴇ ᴡʜᴏʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴜsɪɴɢ ᴛʜᴇ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴs!**

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @Gladiators_Projects
"""
start_caption = f"""
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ.
I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ-ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ!
I'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇsᴛʀᴏʏ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ 🔥🔥🔥
I ᴄᴀɴ sᴘᴀᴍ ᴄᴏɴᴛɪɴᴜᴏsʟʏ ᴡɪᴛʜ ʟᴇss ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀ ᴀɴᴅ ᴡɪᴛʜ ᴍᴏʀᴇ ᴀᴄᴄᴜʀᴀᴄʏ!**

**█▓▒­░⡷⠂ᗰᗩՏTᗴᖇ⠂⢾░▒▓█**
**『 [{DEFAULTUSER}](tg://user?id={OWNER_ID}) 』**

[©️](https://telegra.ph/file/ec3c057fcba5594151601.jpg) @Gladiators_Projects
"""
close_caption = """
**Hᴇʟᴘ ᴍᴇɴᴜ ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ!!**

©️ @Gladiators_Projects
"""
helpbuttons = [
    [
        Button.inline("Sᴘᴀᴍ Cᴍᴅs", data="spamcmds"),
        Button.inline("Dᴇᴠ Cᴍᴅs", data="devcmds")
    ],
    [
        Button.inline("Cʜᴇᴄᴋ Pɪɴɢ", data="pings")
    ],
    [
        Button.inline("Cʟᴏsᴇ", data="close")
    ]
]

help_buttons = [
    [
        Button.inline("Bᴀᴄᴋ", data="back"),
        Button.inline("Cʟᴏsᴇ", data="close")
    ]
]
startbuttons = [
    [
        Button.url("Repo", url="https://github.com/Gladiators-Projects/SpamBot"),
        Button.url("Support", url=f"https://t.me/ProjectsChat"),
    ],
    [
        Button.url("Github Organisation", url="https://github.com/Gladiators-Projects")
    ]
]
  
openbuttons = [
    [
        Button.inline("Oᴘᴇɴ Aɢᴀɪɴ", data="open")
    ]
]

@gladiator.on(events.NewMessage(incoming=True, pattern="^/help(?: |$)(.*)", func=lambda e: e.is_private))
async def alive(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        try:
            await e.reply(help_caption, buttons=helpbuttons)
        except:
            await e.client.send_message(e.chat_id, help_caption, buttons=helpbuttons)
            

@gladiator.on(events.NewMessage(incoming=True, pattern="^/start(?: |$)(.*)"))
async def alive(e):
    try:
        await e.reply(start_caption, buttons=startbuttons)
    except:
        await e.client.send_message(e.chat_id, start_caption, buttons=startbuttons)

@gladiator.on(events.CallbackQuery())
async def chat(event):
    if event.data == b"spamcmds":
        chcksudo = int(event.chat_id)
        if chcksudo not in SUDO_USERS:
            return
        await event.edit(
            spam_caption,
            buttons=help_buttons,
        )
    elif event.data == b"pings":
        chcksudo = int(event.chat_id)
        if chcksudo not in SUDO_USERS:
            return
        ping_start = datetime.now()
        ping_end = datetime.now()
        ms = (ping_end-ping_start).microseconds
        uptime = get_uptime((time.time() - StartTime) * 1000)
        pomg = f"•• Pᴏɴɢ !! ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ : {ms}ᴍs\n⏳ Uᴘᴛɪᴍᴇ - {uptime}"
        await event.edit(
            pomg,
            buttons=help_buttons,
        )
    elif event.data == b"back":
        chcksudo = int(event.chat_id)
        if chcksudo not in SUDO_USERS:
            return
        await event.edit(
            help_caption,
            buttons=helpbuttons,
        )
    elif event.data == b"devcmds":
        chcksudo = int(event.chat_id)
        if chcksudo not in SUDO_USERS:
            return
        await event.edit(
            dev_caption,
            buttons=help_buttons,
        )
    elif event.data == b"open":
        chcksudo = int(event.chat_id)
        if chcksudo not in SUDO_USERS:
            return
        await event.edit(
            help_caption,
            buttons=helpbuttons,
        )
    elif event.data == b"close":
        chcksudo = int(event.chat_id)
        if chcksudo not in SUDO_USERS:
            return
        await event.edit(
            close_caption,
            buttons=openbuttons,
        )
