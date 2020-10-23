import discord
import os
import json
import withyoubot.footer as footer
import withyoubot.start as start
import withyoubot.queries as query
import withyoubot.files as files

print("Starting...")

loop = start.start()

TOKEN = os.getenv('DISCORD_TOKEN')
ADMIN = int(os.getenv('ADMIN_ID'))
client = discord.Client()


@client.event
async def on_ready():
    activity = discord.Activity(name="\"with you\"s, sadly", type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    print("Bot is ready!")


@client.event
async def on_message(message):
    channel = message.channel
    # help command
    if message.content.lower() == ".withyou help":
        commands = json.loads(files.commands_file())['commands']

        embed = discord.Embed(title="\"With You\" Bot",
                              description="The \"with you\":tm: bot is for \"with you\" check in's by pilots on "
                                          "frequency. Feel free to add one to the counter if you hear one!",
                              color=0x013162)
        for x in commands:
            embed.add_field(name=x['name'], value=x['value'], inline=False)

        embed.set_footer(text=footer.footer("The \"with you\" and .killme commands were viewed at"))
        await channel.send(embed=embed)

    # ------------

    # .withyou commands
    if message.content.lower() == ".withyou":
        files.change_file('withyou', '+')

        await query.add_one(loop, 'withyou', message.author.id)

        # We've got our magical number, send the message!
        embed = discord.Embed(title="\"With You\" Bot",
                              type="Rich",
                              description="The \"with you\":tm: counter is now at " + files.read_file('withyou') + ".",
                              color=0x013162)
        embed.set_footer(text=footer.footer("This \"with you\" was submitted at "))
        await channel.send(embed=embed)

    if message.content.lower() == ".withyou rm":
        files.change_file('withyou', '-')

        await query.remove_one(loop, 'withyou', message.author.id)

        # We've got our magical number, send the message!
        embed = discord.Embed(title="\"With You\" Bot", type="Rich",
                              description="A \"with you\" has been removed. The \"with you\":tm: counter is now at " +
                                          files.read_file('withyou') + ".", color=0x013162)
        embed.set_footer(text=footer.footer("This \"with you\" was removed at "))
        await channel.send(embed=embed)

    if message.content.lower() == ".withyou show":
        results = await query.get_values(loop, 'withyou')

        final = []
        for x in results:
            if int(x[2]) > 0:
                final.append([x[1], x[2]])

        # Tell them the number that they want to know!
        embed = discord.Embed(title="\"With You\" Bot", type="Rich",
                              description="The \"with you\":tm: counter is at " + files.read_file('withyou') + ".",
                              color=0x013162)
        for x in final:
            embed.add_field(name="\u200b", value="<@" + str(x[0]) + "> | " + str(x[1]) + " times", inline=True)
        embed.set_footer(text=footer.footer("The \"with you\" counter was viewed at "))
        await channel.send(embed=embed)

    # ------------

    # .killme
    if message.content.lower() == ".killme":
        files.change_file('killme', '+')

        await query.add_one(loop, 'killme', message.author.id)

        # We've got our magical number, send the message!
        embed = discord.Embed(title="\"With You\" Bot", type="Rich",
                              description="There's another `.killme`. The Winnipeg controllers have been over-stressed "
                                          + files.read_file('killme') + " times.", color=0x013162)
        embed.set_footer(text=footer.footer("This .killme was submitted at "))
        await channel.send(embed=embed)

    if message.content.lower() == ".killme rm":
        files.change_file('killme', '-')

        await query.remove_one(loop, 'killme', message.author.id)

        # We've got our magical number, send the message!
        embed = discord.Embed(title="\"With You\" Bot", type="Rich",
                              description="A kill me has been removed. The 'kill me' counter is now at " +
                                          files.read_file('killme') + ".",
                              color=0x013162)
        embed.set_footer(text=footer.footer("This .killme was removed at "))
        await channel.send(embed=embed)

    if message.content.lower() == ".killme show":
        results = await query.get_values(loop, 'killme')

        final = []
        for x in results:
            if int(x[3]) > 0:
                final.append([x[1], x[3]])

        # Tell them the number that they want to know!
        embed = discord.Embed(title="\"With You\" Bot", type="Rich",
                              description="The Winnipeg controllers have been over-stressed " +
                                          files.read_file('killme') + " times.",
                              color=0x013162)
        for x in final:
            embed.add_field(name="\u200b", value="<@" + str(x[0]) + "> | " + str(x[1]) + " times", inline=True)
        embed.set_footer(text=footer.footer("The .killme counter was viewed at "))
        await channel.send(embed=embed)


client.run(TOKEN)
