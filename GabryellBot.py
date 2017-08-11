import asyncio
import discord
from discord.ext import commands

import libraries.user

import os
import traceback
import pickle
import datetime

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

print('[BOT] Connecting...')

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'), description="Commandes")

class Messages:
	"""Commandes Textuelles"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True, no_pm=False)
	async def hi(self, ctx):
		"""Salutations"""
		await self.bot.say("Salut {0.message.author.mention} !".format(ctx))

bot.add_cog(Messages(bot))

@bot.event
async def on_ready():
    print('--------------------------')
    print('[BOT] Logged in as')
    print('[BOT]', bot.user.name)
    print('[BOT]', bot.user.id)
    print('--------------------------')
    await bot.change_presence(game=discord.Game(name='GabryellBot | .help'))

@bot.event
async def on_message(msg):
	data = user.dataGet()
	member = msg.author
	id = member.id
	server = msg.server
	roles = server.roles
	for role in roles:
		if role.id == '':
			firstRole = role
		if role.id == '':
			secondRole = role
		if role.id == '':
			thirdRole = role

	if getFromData(data, id):
		obj = getFromData(data, id)
		obj.add()
		if obj.get() == 500:
			await bot.add_roles(member, [secondRole])
		if obj.get() == 1000:
			await bot.add_roles(member, [thirdRole])
		user.dataUpdate(data, obj, id)
		user.dataSave(data)
	else:
		obj = user.User()
		obj.add()
		user.dataUpdate(data, obj, id)
		user.dataSave(data)

def getToken():
	with open('./config.txt') as f: lines = f.read().splitlines()
	for line in lines:
		if line.startswith('token='):
			getLine = line
			Line = getLine.split('=')
			token = Line[1]
	return token

token = getToken()
bot.run(token)