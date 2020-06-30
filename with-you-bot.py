import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime

print ("Starting...")

bot = commands.Bot(command_prefix='.')

client = discord.Client()
counter = 0
utc_datetime = datetime.datetime.utcnow()

@client.event
async def on_ready():
        activity = discord.Activity(name="\"with you\"s, sadly", type=discord.ActivityType.listening)
        await client.change_presence(activity=activity)
        print("Bot is ready!")
        
@client.event
async def on_message(message):
        channel = message.channel
        global counter
        if message.content.lower() == (".withyou"):
                counter += 1
                embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="The \"with you\":tm: counter is now at " + str(counter) + ".", color=0x013162)
                embed.set_footer(text=("This \"with you\" was submitted at " + str(utc_datetime.strftime ("%H%Mz")) + " | © Kolby Dunning"))
                await channel.send(embed=embed)
        if message.content.lower() == (".withyou rm"):
                counter -= 1
                embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="A \"with you\" has been removed. The \"with you\":tm: counter is now at " + str(counter) + ".", color=0x013162)
                embed.set_footer(text=("This \"with you\" was removed at " + str(utc_datetime.strftime ("%H%Mz")) + " | © Kolby Dunning"))
                await channel.send(embed=embed)
        if message.content.lower() == (".withyou show"):
                embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="The \"with you\":tm: counter is at " + str(counter) + ".", color=0x013162)
                embed.set_footer(text=("The \"with you\" counter was viewed at " + str(utc_datetime.strftime ("%H%Mz")) + " | © Kolby Dunning"))
                await channel.send(embed=embed)
        if message.content.lower() == (".withyou help"):
                embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="The \"with you\":tm: bot is for \"with you\" check in's by pilots on frequency. Feel free to add one to the counter if you hear one!", color=0x013162)
                embed.add_field(name=".withyou", value="Adds 1 \"with you\" to the counter!", inline=False)
                embed.add_field(name=".withyou rm", value="Removes 1 \"with you\" from the counter!", inline=False)
                embed.add_field(name=".withyou show", value="Lets you see the amount of \"with you\"s in the counter!", inline=False)
                embed.add_field(name=".withyou help", value="This one is fairly easy. It shows you the commands for this bot!", inline=False)
                embed.set_footer(text=("The \"with you\" commands were viewed at " + str(utc_datetime.strftime ("%H%Mz")) + " | © Kolby Dunning"))
                await channel.send(embed=embed)
        

client.run("[Redacted for good reason]")
