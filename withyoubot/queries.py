import aiomysql
import os
from dotenv import load_dotenv

load_dotenv()


async def connect(loop):
    return await aiomysql.connect(host=os.getenv('DB_HOST'),
                                  port=3306,
                                  user=os.getenv('DB_USER'),
                                  password=os.getenv('DB_PASSWORD'),
                                  db=os.getenv('DB_DATABASE'),
                                  loop=loop,
                                  autocommit=True)


async def add_one(loop, col, discord_id):
    conn = await connect(loop)
    async with conn.cursor() as cur:
        check = await cur.execute("SELECT * FROM withyou WHERE discord_id = %s", discord_id)
        if check == 0:
            # Set our initial values
            withyou_init = col == 'withyou' and '1' or '0'
            killme_init = col == 'killme' and '1' or '0'

            await cur.execute("INSERT INTO withyou (discord_id, withyou, killme) "
                              "VALUES (%s, %s, %s)", (discord_id, withyou_init, killme_init))
        else:
            await cur.execute(f"UPDATE withyou SET {col} = {col} + 1 WHERE discord_id = %s", discord_id)


async def remove_one(loop, col, discord_id):
    conn = await connect(loop)
    async with conn.cursor(aiomysql.cursors.DictCursor) as cur:
        check = await cur.execute("SELECT * FROM withyou WHERE discord_id = %s", discord_id)
        if check != 0:
            current = await cur.fetchone()
            if current[col] > 0:
                await cur.execute(f"UPDATE withyou SET {col} = {col} - 1 WHERE discord_id = %s", discord_id)


async def get_values(loop, col):
    conn = await connect(loop)
    async with conn.cursor() as cur:
        await cur.execute(f"SELECT * FROM withyou ORDER BY {col} DESC")

        return await cur.fetchall()
