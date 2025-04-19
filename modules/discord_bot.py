import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot connecté : {client.user}")

async def send_alert(channel_id, embed_data, ping_role=None):
    channel = client.get_channel(int(channel_id))
    if ping_role:
        await channel.send(ping_role)
    await channel.send(embed=discord.Embed.from_dict(embed_data))

# client.run(TOKEN)  # Ne pas lancer automatiquement
