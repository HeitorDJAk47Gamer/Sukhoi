import disnake, random
from disnake.ext import commands

sukhoi = commands.Bot(command_prefix = '!',case_insensitive = True, intents=disnake.Intents.all())
@sukhoi.event
async def on_ready():
	Y = sukhoi.latency * 1000
	A = round(Y)
	print(f'Ping atual: {A}')
	print(f'Olha esses canardes de fora {sukhoi.user.id}')


@sukhoi.command()
async def d(ctx, y=0, numero=0, h="nada", mod=0):
  x = []
  while 0 < y:
      x.append(random.randint(1, numero))
      y = (y - 1)
  total = sum(x)
  if numero != 0 and h == "nada":
      await ctx.reply(f"`{total}` <- {x}")
  elif numero != 0 and h == "+":
    ad = (total + mod)
    await ctx.reply(f"`{ad}` <- {x} + {mod}")
  elif numero != 0 and h == "-":
    men = (total - mod)
    await ctx.reply(f"`{men}` <- {x} - {mod}")
  else:
    await ctx.reply ("*Defina um valor válido*")
	
@sukhoi.command()
async def ping(ctx):
  x = sukhoi.latency * 1000
  y = round(x)
  await ctx.send(f"{y} ms")

sukhoi.run('token')