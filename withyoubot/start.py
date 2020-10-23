import aiomysql
import asyncio
import os
from dotenv import load_dotenv


def start():
    if os.path.exists('.env'):
        load_dotenv()
        pass
    else:
        f = open('.env', 'x')
        f.write("# .env\n"
                "DISCORD_TOKEN=\n"
                "GUILD_ID=\n"
                "ADMIN_ID=\n\n"
                "# Database stuff\n"
                "DB_HOST=\n"
                "DB_USER=\n"
                "DB_PASSWORD=\n"
                "DB_DATABASE=")
        f.close()
        print("You need to fill in the fields in the .env file (it's in the withyoubot folder).")
        exit()

    if os.path.exists('withyou.txt'):
        pass
    else:
        f = open('withyou.txt', 'x')
        f.write("0")
        f.close()

    if os.path.exists('killme.txt'):
        pass
    else:
        f = open('killme.txt', 'x')
        f.write("0")
        f.close()

    # Create DB table if it doesn't exist
    async def make_database(loop):
        db = await aiomysql.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            db=os.getenv("DB_DATABASE"),
            port=3306,
            loop=loop
        )

        async with db.cursor() as table_check:
            check = await table_check.execute("SHOW TABLES LIKE 'withyou'")
            if check == 0:
                print("Creating DB table...")
                await table_check.execute("CREATE TABLE withyou (id INT AUTO_INCREMENT PRIMARY KEY, "
                                          "discord_id BIGINT NOT NULL, "
                                          "withyou INT NOT NULL, "
                                          "killme INT NOT NULL)")
                await db.commit()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_database(loop))
    return loop
