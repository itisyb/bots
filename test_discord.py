import discord
import youtube_dl
from discord.ext import commands
import asyncio
import os


def bot():
    client = commands.Bot(command_prefix='.')
    client.remove_command('help')

    players = {}
    @client.event
    async def on_ready():
        print('Bot is ready')

    @client.command(pass_context=True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

    @client.command(pass_context=True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()

    @client.command(pass_context=True)
    async def play(ctx,url):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id]= player
        player.start()

    @client.event
    async def on_member_join(member):

        await client.send_message(member,"Hello {}\n WELCOME TO OUR SERVER PLEASE type '.help' in the server to see awavilable commands".format(member))
    



    @client.command(pass_context=True)
    async def help(ctx):
        author = ctx.message.author 
        emb = discord.Embed(
            
        colour= discord.Colour.blue()
        )
        emb.set_author(name='MUSIC BOT HELP')
        
        emb.add_field(name='WELCOME TO OUR SERVER I M HAPPY TO HELP :)',value='->',inline=True)
        
        emb.add_field(name='.play + url',value='it playes youtube video \n',inline = False)
        
        emb.add_field(name='.Pause ',value='it pauses the music \n',inline = False)
        
        emb.add_field(name='.Resume ',value='it resume the music \n',inline = False)
        emb.add_field(name='.stop',value='it stops the music \n',inline = False)
        
        await client.send_message(author,embed=emb)

    @client.command(pass_context=True)
    async def pause(ctx):
        id = ctx.message.server.id
        players[id].pause()
    @client.command(pass_context=True)
    async def stop(ctx):
        id = ctx.message.server.id
        players[id].stop()
    @client.command(pass_context=True)
    async def resume(ctx):
        id = ctx.message.server.id
        players[id].resume()

    client.run(os.ge.getenv('TOKEN'))

if __name__ == "__main__":
    bot()
