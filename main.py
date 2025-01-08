import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        print("bot mentioned")
        await message.channel.send("Hello you mentioned me")

    if message.content.startswith("hello"):
        print("bot recieved hello")
        await message.channel.send("Hello!")

    if message.content.startswith("How are you?"):
        await message.channel.send("I'm fine and you?")

    if message.content.startswith("I'm fine too"):
        await message.channel.send("Glad to hear that")

bot_key = os.getenv("BOT_KEY")

client.run(bot_key)
