import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('help'):
        await message.channel.send(f'pastikan kalian menguanakan tanda $ untuk menanyakan bot harus buang sampah di mana  cnth("$sampah kertas")')
    if message.author == client.user:
        return
    if message.content.startswith('$sampah plastic'):
        await message.channel.send(f'buang di tempat sampah anorganic')
    elif  message.content.startswith('$sampah kertas'):
        await message.channel.send(f'buang di tempat sampah kertas')
    elif  message.content.startswith('$sampah B3'):
        await message.channel.send(f'buang di tempat sampah B3')
    elif  message.content.startswith('$sampah tanaman'):
        await message.channel.send(f'buang di tempat sampah organic')    
client.run("MTEyOTU5MDk3NDQ3NDEwODk5OQ.GtclH2.ayRcL6gmKykKiA4EFgyYyvi3KvAIyndErqRK58")
