# imports
import discord
import arxiv
from discord.ext import tasks
from datetime import datetime

# create new discord bot
# when the bot is connected (on_ready), fetch the papers
class MyClient(discord.Client):

  # start the loop
  async def on_ready(self):
    self.fetch_arxiv_papers.start()
    print(f'Logged on as {self.user}!')

  @tasks.loop(minutes=720.0)
  async def fetch_arxiv_papers(self):
    # replace 'channel_id' with the ID of your channel (must be an integer)
    channel = self.get_channel(channel_id)

    search = arxiv.Search(query="AI",
                          max_results=4,
                          sort_by=arxiv.SortCriterion.SubmittedDate)

    # Print the paper details, one msg per paper
    for result in search.get():
      clean_date = result.published.strftime("%Y-%m-%d")
      await channel.send(f"**New paper published:**\n\n"
                         f"**Title:** {result.title}\n"
                         f"**Date:** {clean_date}\n\n"
                         f"**Abstract:** {result.summary}\n\n"
                         f"**PDF URL:** {result.pdf_url}\n\n"
                         "-------------------------")

intents = discord.Intents.default()
intents.messages = True

# run the bot
client = MyClient(intents=intents)
client.run(
  'discord-bot-code-here')

# this is the part that allows it to run 24/7
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return "Bot up and running"


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, port=8080)
