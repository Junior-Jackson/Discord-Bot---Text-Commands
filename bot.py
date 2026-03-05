import discord
import requests
import json
import random
import asyncio
def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return
    content = message.content.lower()
    if content.startswith('$meme'):
      await message.channel.send(get_meme())
    if content.startswith('$hello'):
      await message.channel.send('Hello World!')
    if content.startswith('$lets play rock paper scissor'):
      await message.channel.send("Lets Play! Type **rock**, **paper, or **scissor**.")
    def check(m):
        return (
        m.author == message.author
        and m.channel == message.channel
        and m.content.lower() in ['rock','paper','scissor']
        )
    try:
        user_msg = await self.wait_for('message',check=check, timeout=20)
    except asyncio.TimeoutError:
        await message.channel.send("You took too long! Game Cancelled.")
        return
    user_choice = user_msg.content.lower()
    bot_choice = random.choice(['rock','paper','scissor'])
    await message.channel.send(f"i choose **{bot_choice}**!")
    if user_choice == bot_choice:
        result = "its a tie"
    elif (
       (user_choice == "rock"and bot_choice == "scissor")or
       (user_choice =="paper" and bot_choice =="rock") or 
       (user_choice == "scissor" and bot_choice =="paper")
    ):
       result = "You win!"
    else:
       result = "I Win !"
    await message.channel.send(result)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('insert your discord token here') #insert your discord token here.