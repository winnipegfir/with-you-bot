import discord
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

database = mysql.connector.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_DATABASE")
)

with_you = database.cursor()
with_you.execute("SELECT * FROM withyou")
with_you_results = with_you.fetchall()

intents = discord.Intents.default()
intents.members = True
client = discord.Client()


@client.event
async def on_ready():
    print("Starting user removal cronjob.")
    for x in with_you_results:
        if client.get_user(x[1]) is not None:
            print("-> " + str(x[1]) + " is in the server. Skipping.")
            pass
        else:
            with_you.execute("DELETE FROM withyou WHERE discord_id = " + str(x[1]))
            print("-> Deleting ID " + str(x[1]) + " from database as they are not in the server.")

    database.commit()
    print("Done!")
    await client.close()

client.run(os.getenv('DISCORD_TOKEN'))
quit()
