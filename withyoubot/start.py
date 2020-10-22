import mysql.connector
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
        print("You need to fill in the fields in the .env file.")
        exit()

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

    # Create DB table if it doesn't exist
    db = mysql.connector.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DATABASE")
    )

    table_check = db.cursor()
    table_check.execute("SHOW TABLES LIKE 'withyou'")
    if not table_check.fetchone():
        print("Creating DB table")
        table_check.execute("CREATE TABLE withyou (id INT AUTO_INCREMENT PRIMARY KEY, "
                            "discord_id BIGINT NOT NULL, "
                            "withyou INT NOT NULL, "
                            "killme INT NOT NULL)")
        db.commit()