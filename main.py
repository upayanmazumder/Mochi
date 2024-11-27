import os
from dotenv import load_dotenv
import discord

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    raise ValueError("Bot token not found. Make sure the BOT_TOKEN is set in your .env file.")

intents = discord.Intents.default()
intents.messages = True

class MyBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

bot = MyBot(intents=intents)

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Error starting the bot: {e}")
