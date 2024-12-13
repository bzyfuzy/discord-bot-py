import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
token = os.getenv('DISCORD_TOKEN')

# Create the bot instance
bot = commands.Bot(command_prefix="!")

# Event triggered when the bot has connected to Discord
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# A simple command
@bot.command()
async def greet(ctx):
    await ctx.send('Hello!')

@bot.command()
async def roll(ctx, sides: int):
    import random
    roll = random.randint(1, sides)
    await ctx.send(f'You rolled a {roll} on a {sides}-sided die!')

# Run the bot with your token
bot.run(token)