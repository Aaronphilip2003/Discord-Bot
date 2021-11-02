import discord
import os
from discord.ext import commands


client=discord.Client()
my_secret=os.environ['TOKEN']
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def hi(ctx):
    await ctx.send("wassup")

@bot.command(pass_context=True)
async def on_help(ctx):
	await ctx.send("$add ")
	await ctx.send("$subt")
	await ctx.send("$mult")
	await ctx.send("$div ")
	await ctx.send("$rem ")

@bot.command(pass_context=True)
async def add(ctx,arg1,arg2):
	await ctx.send(f"Addition: {float(arg1)+float(arg2)}")

@bot.command(pass_context=True)
async def subt(ctx,arg1,arg2):
	await ctx.send(f"Difference: {float(arg1)-float(arg2)}")

@bot.command(pass_context=True)
async def mult(ctx,arg1,arg2):
	await ctx.send(f"Product: {float(arg1)*float(arg2)}")

@bot.command(pass_context=True)
async def div(ctx,arg1,arg2):
	await ctx.send(f"Quotient: {float(arg1)/float(arg2)}")

@bot.command(pass_context=True)
async def rem(ctx,arg1,arg2):
	await ctx.send(f"Remainder: {float(arg1)%float(arg2)}")


bot.run(os.getenv('TOKEN'))

client.run(os.getenv('TOKEN'))
