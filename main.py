import os
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '*')
greetings = []

def get_greeting():
  if not greetings:
    file = open("bye.txt", "r")
    for line in file:
      greetings.append(line)
    file.close()
  return random.choice(greetings)

@client.command()
async def clear(ctx, amount: int):
  if amount < 1:
    return
  await ctx.channel.purge(limit=amount+1)
  await ctx.send("{} messages cleared.".format(amount))

@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.lower() == "bye":
    await message.channel.send(get_greeting())
  await client.process_commands(message)
  
initial_extensions = []
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
  for extension in initial_extensions:
    client.load_extension(extension)

client.run(os.getenv("TOKEN"))