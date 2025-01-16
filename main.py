import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if bot.user in message.mentions:
        print("bot mentioned")
        await message.channel.send("Hello you mentioned me")

    if content.startswith("hello"):
        print("bot recieved hello")
        await message.channel.send("Hello!")

    if content.startswith("How are you?"):
        await message.channel.send("I'm fine and you?")

    if content.startswith("I'm fine too"):
        await message.channel.send("Glad to hear that")

    await bot.process_commands(message)

@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(f"You said {arg}")


bot_key = os.getenv("BOT_KEY")

bot.run(bot_key)
