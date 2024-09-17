import discord
from discord.ext import commands
import pip freeze > requirements.txt

# Define the bot and enable all necessary intents, including message content intent
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Define the dice command
@bot.command()
async def dice(ctx, n: int):
    if n <= 0:
        await ctx.send("Please enter a positive number greater than 0!")
        return

    # Roll one die in the range of 1 to n
    roll = random.randint(1, n)
    
    await ctx.send(f'You rolled a die with a range of 1 to {n}: {roll}')

# Run the bot with your token
bot.run('MTI4NTY4NDMyNzIxNjMyMDUxMg.GO4mdp.zbJb9gntd2D-qXJufp-W0LanR0pVaAOHg3Kf6I')