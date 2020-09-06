# with-you-bot
An overengineered counter that allows for our controllers to track the "with you" check ins on frequency, as well as the times they have been overstressed while controlling.

This is a Python Discord bot. It was made in Python 3.8 with the Discord class. It also features a database connection (using MySQL) for tracking how many times a specific user has used the commands.

It also has a cron script, that can be used at any frequency you'd like. It runs through your database set of users and checks if they are in the guild, if they aren't, 👋. This is **not necessary** for the bot to run, but it can be good for keeping your database clean.

### Initial Setup
1. Clone the repository
1. Run `with-you-bot.py`
1. Fill in the fields in `.env`
1. Run `with-you-bot.py` again, it should automatically create a database

Any questions, comments or concerns can be directed to virtualwinnipegfir@gmail.com

### Links:

Discord Developer (used for creating bot and making token): https://discord.com/developers
Download Python at: https://www.python.org/downloads/

### Screenshots
![.withyou](https://i.imgur.com/cCH5M7l.png)

![.withyou rm](https://i.imgur.com/L2Ui17G.png)

![.withyou show](https://i.imgur.com/s5uFVvB.png)

![.withyou num #](https://i.imgur.com/KdiW9zJ.png)