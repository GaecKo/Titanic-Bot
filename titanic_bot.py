from discord.ext import commands
import discord
import asyncio, sys, os, time
from dotenv import load_dotenv

from assets.players import *
from assets.wars import *
load_dotenv()

war_channel = 957400070418997292

def war_checkup():
	while True:
		if is_there_war():
			time.sleep(2)
			attributes = someone_dead()
			if attributes[0] == False:
				continue
			else:
				channel = bot.get_channel(war_channel)
				channel.send(get_war_info(attributes[1]))
		


class CustomHelpCommand(commands.HelpCommand):
	def __init__(self):
		super().__init__()
	async def send_bot_help(self, mapping):	
		await self.get_destination().send(help())

	async def send_cog_help(self, cog):	
		await self.get_destination().send(help())

	async def send_group_help(self, group):	
		await self.get_destination().send(help())

	async def send_command_help(self, command):	
		await self.get_destination().send(help())

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix=".", help_command=CustomHelpCommand())

@bot.event
async def on_ready():
	print(f"{bot.user} is ready and has started running")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    await bot.process_commands(msg)

# ------- WORKING TEST ------- #
@bot.command(name='ready') 
async def ready(ctx):
    await ctx.send(f"{bot.user} is ready and running!")

@bot.command(name='players')
async def initiate_players(ctx):
	for guild in bot.guilds:
		for member in guild.members:
			create_player(member.id)
			
	await ctx.send("All users are now in the database!")

bot.run(os.getenv("TOKEN"))
