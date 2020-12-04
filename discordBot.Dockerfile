FROM python:3.6

WORKDIR /app/discordBot/
COPY . /app

RUN pip install discord.py
RUN pip install requests
CMD python bot.py 