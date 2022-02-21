import asyncio
from _ast import Lambda
import random
import discord
from discord import embeds
from discord import Embed
import discord
import discord
from discord import Member, Guild


client = discord.Client()
time = 10
bump = client.get_channel(906190405928886342)

#embeds
rickroll=discord.Embed(title="Welcome Gift!", description="Claim your welcome gift now! (Unclaimeble after 5 Minutes)", color=0x14a5b8)
rickroll.add_field(name="Link:", value="https://bit.ly/InnerCircleWelcomeGift", inline=False)

help=discord.Embed(title="Commands of CircleBot", description="Here is the help-list of this bot!", color=0x12bdd3)
help.add_field(name="!help", value="Shows this page", inline=False)
help.add_field(name="!dev", value="Shows the developer of this bot", inline=False)
help.add_field(name="!ping", value="Shows the latency of this bot", inline=False)
help.add_field(name="!welcomegift", value="Shows your welcome gift (New users only)", inline=True)
help.add_field(name="!fractions", value="Shows the fractions of the SMP", inline=False)
help.add_field(name="!create-a-fraction", value="Shows the fraction-create link", inline=False)

smp=discord.Embed(title="SMP", description="The Server IP is 185.248.140.237. Connect via Version 1.18.1!", color=0x12bdd3)

dev=discord.Embed()
dev.add_field(name="CircleBot Developer:", value="The Developer of this Bot is **@joshiy13#7277**", inline=False)

fractions=discord.Embed()
fractions.add_field(name="Fractions:", value="Right now there arent any fractions on the SMP. You can create a fraction if you have a team with at least 4 Players in it!", inline=False)

create_a_fraction=discord.Embed()
create_a_fraction.add_field(name="Create a Fraction:", value="You can create your Fraction here: https://bit.ly/Create-A-Fraction", inline=False)


@client.event
async def on_ready():
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("Coded by joshiy13#7277"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("Pretty cool right?"), status=discord.Status.online)
        await asyncio.sleep(5)
       


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if "!help" in message.content:
        await message.channel.send(embed=help)
    if "!dev" in message.content:
        await message.channel.send(embed=dev)
    if "!ping" in message.content:
        await message.channel.send(f"Pong! {round(client.latency * 1000)}ms")
    if "!welcomegift" in message.content:
            await message.channel.send(embed=rickroll)
    if "!smp" in message.content:
        await message.channel.send(embed=smp)
    if "!fractions" in message.content:
        await message.channel.send(embed=fractions)
    if "!create-a-fraction" in message.content: 
        await message.channel.send(embed=create_a_fraction)


    


client.run("TOKEN")


