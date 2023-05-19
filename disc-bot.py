import nextcord
from nextcord.ext import commands
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

intents = nextcord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.event
async def on_message(message):
    mentioned_user = await bot.fetch_user(
        309183407219539989
    )  # Replace with the ID of the user you want to detect

    # Load settings from a JSON file
    with open("settings.json", "r") as f:
        settings = json.load(f)

    response_text = settings.get("response_text", "Default response")

    if response_text != "null" and mentioned_user in message.mentions:
        await message.channel.send(response_text)

    await bot.process_commands(message)


bot.run(os.getenv("BOT_TOKEN"))
