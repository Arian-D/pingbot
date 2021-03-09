import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message : discord.Message):
        print(message.content)
        voice = message.author.voice
        if voice and message.content.startswith("@vc") and message.mentions == []:
            await message.channel.send(', '.join(f"<@!{u}>" for u in voice.channel.voice_states.keys()), delete_after = 5)
        
        if message.content == 'ping':
            await message.channel.send('pong')


client = MyClient()
# TODO: Add error handling
client.run(open("token.txt", 'r').read())
