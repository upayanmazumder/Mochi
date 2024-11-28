import os
from dotenv import load_dotenv
import discord
from logger import log

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    log("Bot token not found. Make sure the BOT_TOKEN is set in your .env file.", level="error")
    raise ValueError("Bot token not found.")

intents = discord.Intents.default()
intents.message_content = True

class MyBot(discord.Client):
    async def on_ready(self):
        log(f"Logged in as {self.user}", level="info")

    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore self messages

bot = MyBot(intents=intents)

if __name__ == "__main__":
    try:
        log("Starting the bot...", level="info")
        bot.run(TOKEN)
    except Exception as e:
        log(f"Error starting the bot: {e}", level="critical")
