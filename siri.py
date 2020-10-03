import discord
from discord.ext import commands
from PingPongTool import PingPong
from random import randint
import koreanbots

def RandomColor():
    return randint(0, 0xFFFFFF)

TOKEN = "토큰"
Authorization = "핑퐁빌더 api 토큰"
URL = "핑퐁빌더 api 링크"

bot = commands.Bot(command_prefix=['시리야 '])
Ping = PingPong(URL, Authorization)


@bot.listen()
async def on_command_error(ctx, error):
    if type(error) is commands.errors.CommandNotFound:
        data = await Ping.Pong(ctx.author.id, ctx.message.content, NoTopic=False)
        embed = discord.Embed(
            title="인공지능",
            description=data['text'],
            color=RandomColor()
        )
        embed.set_footer(text="Using PingPongTool(Minibox님의 핑퐁툴사용)")
        if data['image']:
            embed.set_image(url=data['image'])
        await ctx.send(embed=embed)


@bot.command(name="따라해")
async def Echo(ctx, *, text: str):
    await ctx.send(text)

@bot.command(name="hellothisisverification")
async def Echo(ctx):
    await ctx.send("유저닉네임#유저태그(유저ID)")

@bot.event
async def on_ready():
    print('시리 준비 완료')
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('시리야 할말'))

bot.run(TOKEN)
