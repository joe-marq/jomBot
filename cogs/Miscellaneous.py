import discord
import random
from discord.ext import commands
import requests
import json

class Miscellaneous(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def inspire(self, ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    await ctx.send(quote)

def setup(client):
  client.add_cog(Miscellaneous(client))