from discord.ext import commands
import asyncio, sys, os
from dotenv import load_dotenv
load_dotenv()

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