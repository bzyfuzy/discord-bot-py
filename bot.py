import re
import os
import random
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

# Enhanced dice rolling command
@bot.command()
async def dice(ctx, dice_command: str):
    # Example input: "2d6+3", "d20", "3d8-2"
    match = re.match(r"(\d*)d(\d+)([+-]\d+)?", dice_command)
    
    if match:
        num_dice = int(match.group(1) or 1)  # Default to 1 die if not specified
        sides = int(match.group(2))  # Number of sides on the dice
        modifier = match.group(3) if match.group(3) else 0  # Optional modifier

        # Roll the dice
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(rolls)

        # Apply the modifier if present
        if modifier:
            total += int(modifier)

        # Prepare result string
        result = f"Rolling {num_dice}d{sides}{modifier}: {', '.join(map(str, rolls))} => Total: {total}"
        
        # Send the result back to the Discord channel
        await ctx.send(result)
    else:
        await ctx.send("Invalid dice format! Use something like `!roll 2d6+3` or `!roll d20`.")

if __name__ == "__main__":
    bot.run(token)
