import discord 
import os 
import requests
import json
from replit import db
import random



client=discord.Client()
my_secret=os.environ['TOKEN']

sad_words=["sad","depressed","unhappy","angry","miserable","depressing","lost","sorrowful","dejected","regretful","alone","lonely"]

starter_encouragements=["Cheer Up!",
"Hang in there",
"You are great person /bot!"]


def get_quote():
	response=requests.get("https://zenquotes.io/api/random")
	json_data=json.loads(response.text)
	quote=json_data[0]['q'] + " -" + json_data[0]['a']
	return(quote)

def update_encouragements(encouraging_message):
	if "encouragements" in db.keys():
		encouragements = db["encouragements"]
		encouragements.append(encouraging_message)
		db["encouragements"]=encouragements
	else:
		db["encouragements"]=[encouraging_message]

def delete_encouragement(index):
	encouragements=db["encouragements"]
	if len(encouragements)>index:
		del encouragements[index]
	db["encouragements"]=encouragements


@client.event
async def on_ready():
	print("You are logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello' or '$Hello'):
		await message.channel.send("Hello!")

	if message.content.startswith('$bye' or '$Bye'):
		await message.channel.send("Bye!")

	if message.content.startswith("$inspire"):
		quote=get_quote()
		await message.channel.send(quote)
	

	options=starter_encouragements
	if "encouragements" in db.keys():
		options=options+db["encouragements"]

	if any(word in message.content for word in sad_words):
		await message.channel.send(random.choice(options))
	

client.run(os.getenv('TOKEN'))


	