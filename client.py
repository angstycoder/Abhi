import discord
import asyncio
import json
import  random
client = discord.Client()

def ran():
    r=int(random.random()*10)
    return (r)
with open('token.json') as secret:
    token = json.load(secret)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('?a count'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('?a sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    resp=['What!','What do you mean by that??',
          'You need a random number?',
          'Pfft no!','Me no do it!!',
          'Its not like i get paid for this -_-']
    if message.content.startswith('?a random'):
        tp = await client.send_message(message.channel, 'Random Number? ')
        while resp:
            a=random.choice(resp)
            tp = await client.edit_message(tp,a)
            resp.remove(a)
            await asyncio.sleep(2.5)

        await asyncio.sleep(1)
        await client.edit_message(tp,'It is {}.'.format(ran()))
    if message.content.startswith('>.<'):
        await client.send_message(message.author,'Dont you dare!')
        await client.add_reaction(message,'\N{THUMBS UP SIGN}')



client.run(token)
