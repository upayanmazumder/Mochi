import os
from dotenv import load_dotenv
import discord
from logger import log

# Load environment variables
load_dotenv()

# Retrieve the bot token
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    log("Bot token not found. Make sure the BOT_TOKEN is set in your .env file.", level="error")
    raise ValueError("Bot token not found.")

# Configure intents for the bot
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

class MyBot(discord.Client):
    async def on_ready(self):
        log(f"Logged in as {self.user}", level="info")

    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself

        # Respond to "ping" messages
        if message.content.lower() == "ping":
            log(f"Received 'ping' from {message.author}. Sending 'Pong!'", level="debug")
            await message.channel.send("Pong!")

# Instantiate the bot
bot = MyBot(intents=intents)

if __name__ == "__main__":
    try:
        log("Starting the bot...", level="info")
        bot.run(TOKEN)
    except Exception as e:
        log(f"Error starting the bot: {e}", level="critical")
