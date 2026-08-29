import discord
from discord.ext import commands
from discord import app_commands
import time

intents = discord.Intents.all()

token = ""

prefix="$"

max_uses = 3
wseconds = 5*30
bseconds = 15*60

userusage = {}

class SyraBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(
            command_prefix=prefix,
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        await self.tree.sync()
        print("Commands synced")

bot = SyraBot()

@bot.event
async def on_ready():
    print("""
  _________                     
 /   _____/__.__.____________   
 \\_____  <   |  |\\_  __ \\__  \\  
 /        \\___  | |  | \\// __ \\_
/_______  / ____| |__|  (____  /
        \\/\\/                 \\/ 
(External app)
""")

pingpm = """
```‎            〚₮ᴋ₮〛𝐓𝐡𝐞 𝐊𝐧𝐢𝐠𝐡𝐭𝐬 𝐓𝐞𝐦𝐩𝐥𝐚𝐫〚₮ᴋ₮〛
‎                          𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗕𝗘𝗘𝗡 𝗥𝗔𝗜𝗗𝗘𝗗
‎                                       〘💎〙
                        • ʀᴀɪᴅᴇᴅ ʙʏ ᴛᴋᴛ
                        • ᴊᴏɪɴ ᴜꜱ ꜰᴏʀ ᴅᴀɪʟʏ ɴᴜᴋᴇꜱ + ʀᴀɪᴅꜱ
                        • ᴅᴀɪʟʏ ɴᴜᴋᴇꜱ
                        • ᴊᴏɪɴ ᴛʜᴇ ᴋɴɪɢʜᴛꜱ ᴛᴇᴍᴘʟᴀʀ ᴀɴᴅ ᴄᴏɴQᴜᴇʀ
                        • ꜱᴇʀᴠᴇʀ ᴛᴀɢ
‎                                       〘💎〙
```
||@everyone||
https://discord.gg/S9Kv9pp8pp
"""

pm = """
```‎            〚₮ᴋ₮〛𝐓𝐡𝐞 𝐊𝐧𝐢𝐠𝐡𝐭𝐬 𝐓𝐞𝐦𝐩𝐥𝐚𝐫〚₮ᴋ₮〛
‎                          𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗕𝗘𝗘𝗡 𝗥𝗔𝗜𝗗𝗘𝗗
‎                                       〘💎〙
                        • ʀᴀɪᴅᴇᴅ ʙʏ ᴛᴋᴛ
                        • ᴊᴏɪɴ ᴜꜱ ꜰᴏʀ ᴅᴀɪʟʏ ɴᴜᴋᴇꜱ + ʀᴀɪᴅꜱ
                        • ᴅᴀɪʟʏ ɴᴜᴋᴇꜱ
                        • ᴊᴏɪɴ ᴛʜᴇ ᴋɴɪɢʜᴛꜱ ᴛᴇᴍᴘʟᴀʀ ᴀɴᴅ ᴄᴏɴQᴜᴇʀ
                        • ꜱᴇʀᴠᴇʀ ᴛᴀɢ
‎                                       〘💎〙
```
https://discord.gg/S9Kv9pp8pp
"""
    
@bot.tree.command(
    name="raid",
    description="sends a set of raid messages"
)
async def raid(interaction: discord.Interaction):
    allowed, remaining = check_cooldown(interaction.user.id)
    if not allowed:
        minutes = remaining // 60
        seconds = remaining % 60
        await interaction.response.send_message(
            f"Ur on cooldown.\n"
            f"Try again in {minutes}m {seconds}s",
            ephemeral=True
        )
        return
    await interaction.response.send_message(pm)
    print(f"Raiding a server")
    for i in range(5):
        await interaction.followup.send(pm)
    print(f"Raided server")
        
@bot.tree.command(
    name="pingraid",
    description="use if @everyone enabled"
)
async def raid(interaction: discord.Interaction):
    allowed, remaining = check_cooldown(interaction.user.id)
    if not allowed:
        minutes = remaining // 60
        seconds = remaining % 60
        await interaction.response.send_message(
            f"Ur on cooldown.\n"
            f"Try again in {minutes}m {seconds}s",
            ephemeral=True
        )
        return
    await interaction.response.send_message(pingpm)
    print(f"Raiding a server")
    for i in range(5):
        await interaction.followup.send(pingpm)
    print(f"Successfully raided")

############################################################

def check_cooldown(user_id: int):
    now = time.time()
    data = userusage.setdefault(
        user_id,
        {"uses": [], "blocked_until": None}
    )
    if data["blocked_until"]:
        if now < data["blocked_until"]:
            remaining = int(data["blocked_until"] - now)
            return False, remaining
        else:
            data["blocked_until"] = None
            data["uses"].clear()

    data["uses"] = [
        t for t in data ["uses"]
        if now - t < wseconds
    ]
    if len(data["uses"]) >=max_uses:
        data["blocked_until"] = now + bseconds
    data["uses"].append(now)
    return True, None

bot.run(token)
    
