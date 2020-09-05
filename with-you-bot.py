import discord

import os
from dotenv import load_dotenv

import datetime

print("Starting...")

if os.path.exists('.env'):
    pass
else:
    f = open('.env', 'x')
    f.write("# .env\nDISCORD_TOKEN=\nADMIN_ID=")
    f.close()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ADMIN = int(os.getenv('ADMIN_ID'))

client = discord.Client()

if os.path.exists('counter.txt'):
    pass
else:
    f = open('counter.txt', 'x')
    f.write("0")
    f.close()

if os.path.exists('killme.txt'):
    pass
else:
    f = open('killme.txt', 'x')
    f.write("0")
    f.close()


@client.event
async def on_ready():
    activity = discord.Activity(name="\"with you\"s, sadly", type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    print("Bot is ready!")


@client.event
async def on_message(message):
    channel = message.channel
    utc_datetime = datetime.datetime.utcnow()
    # .withyou
    global counter
    if message.content.lower() == (".withyou"):
        # Read the file, add one, read again
        with open('./counter.txt', 'r') as file:
            counter = file.read()
        with open('./counter.txt', 'w') as file:
            file.write(str(int(counter) + 1))
        with open('./counter.txt', 'r') as file:
            counter = file.read()

        # We've got our magical number, send the message!
        embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="The \"with you\":tm: counter is now at " + str(counter) + ".", color=0x013162)
        embed.set_footer(text=("This \"with you\" was submitted at " + str(utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
        await channel.send(embed=embed)

    if message.content.lower() == (".withyou rm"):
        # Read the file, remove one, read again
        with open('./counter.txt', 'r') as file:
            counter = file.read()
        with open('./counter.txt', 'w') as file:
            file.write(str(int(counter) - 1))
        with open('./counter.txt', 'r') as file:
            counter = file.read()

        # We've got our magical number, send the message!
        embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="A \"with you\" has been removed. The \"with you\":tm: counter is now at " + str(counter) + ".", color=0x013162)
        embed.set_footer(text=("This \"with you\" was removed at " + str(utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
        await channel.send(embed=embed)

    if message.content.lower() == (".withyou show"):
        # Read the file
        with open('./counter.txt', 'r') as file:
            counter = file.read()

        # Tell them the number that they want to know!
        embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="The \"with you\":tm: counter is at " + str(counter) + ".", color=0x013162)
        embed.set_footer(text=("The \"with you\" counter was viewed at " + str(utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
        await channel.send(embed=embed)
    if message.content.lower() == (".withyou help"):
        embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="The \"with you\":tm: bot is for \"with you\" check in's by pilots on frequency. Feel free to add one to the counter if you hear one!", color=0x013162)
        embed.add_field(name=".withyou", value="Adds 1 \"with you\" to the counter!", inline=False)
        embed.add_field(name=".withyou rm", value="Removes 1 \"with you\" from the counter!", inline=False)
        embed.add_field(name=".withyou show", value="Lets you see the amount of \"with you\"s in the counter!", inline=False)
        embed.add_field(name=".withyou help", value="This one is fairly easy. It shows you the commands for this bot!", inline=False)
        embed.add_field(name="\u200b", value="Introducing .killme! Made for the times you just want to die while controlling!", inline=False)
        embed.add_field(name=".killme", value="Adds 1 .killme to the counter!", inline=False)
        embed.add_field(name=".killme show", value="Displays the amount of times our controllers have been over-stressed by VATSIM's pilots.", inline=False)
        embed.set_footer(text=("The \"with you\" and .killme commands were viewed at " + str(utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
        await channel.send(embed=embed)

    if message.content.lower().startswith(".withyou num "):
        # Check if it's me sending the message
        if message.author.id != ADMIN:
            return
        else:
            user = client.get_user(ADMIN)
            new = message.content[13:]
            try:
                int(new)
                pass
            except ValueError:
                embed = discord.Embed(title=("\"With You\" Bot"), type="Rich",
                                      description="Uh oh. The number need to be an integer.", color=0xFF0000)
                embed.set_footer(text=("The \"with you\" counter was set at " + str(
                    utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
                await user.send(embed=embed)
                return

            # Overwrite the current number with the specified
            with open('./counter.txt', 'w') as file:
                file.write(new)
            with open('./counter.txt', 'r') as file:
                counter = file.read()

            # Tell me so I know it works!
            embed = discord.Embed(title=("\"With You\" Bot"), type="Rich",
                                  description="The \"with you\":tm: counter has been set at " + str(counter) + ".",
                                  color=0x013162)
            embed.set_footer(text=("The \"with you\" counter was set at " + str(
                utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
            await user.send(embed=embed)

    # .killme
    if message.content.lower() == (".killme"):
        # Read the file, add one, read again
        with open('./killme.txt', 'r') as file:
            killme = file.read()
        with open('./killme.txt', 'w') as file:
            file.write(str(int(killme) + 1))
        with open('./killme.txt', 'r') as file:
            killme = file.read()

        # We've got our magical number, send the message!
        embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="There's another `.killme`. The Winnipeg controllers have been over-stressed " + str(killme) + " times.", color=0x013162)
        embed.set_footer(text=("This .killme was submitted at " + str(utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
        await channel.send(embed=embed)

    if message.content.lower() == (".killme show"):
        # Read the file
        with open('./killme.txt', 'r') as file:
            killme = file.read()

        # Tell them the number that they want to know!
        embed = discord.Embed(title=("\"With You\" Bot"), type="Rich", description="The Winnipeg controllers have been over-stressed " + str(killme) + " times.", color=0x013162)
        embed.set_footer(text=("The .killme counter was viewed at " + str(utc_datetime.strftime("%H%Mz")) + " | © Kolby Dunning"))
        await channel.send(embed=embed)


client.run(TOKEN)
