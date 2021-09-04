## Create main.py file


# Import modules
import datetime
import discord  # discord.py
import os  # os
import requests  # requests
import json  # json
from discord.ext import commands  # discord.ext.commands
from dotenv import load_dotenv  # .env
from weather import weather_module  # weather.py


client = commands.Bot(command_prefix="$")
load_dotenv()
# Load token from .env file
TOKEN = os.getenv("DISCORD_TOKEN")


# Funcion para comprobar si coincide el usuario del mensaje con el mensaje enviado
# @param message: mensaje enviado
# @param user: usuario del mensaje
# @return: True si coincide, False en caso contrario
# @return: None si no se ha podido obtener el usuario
# @return: None si no se ha podido obtener el mensaje


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$consuelo"):
        await message.channel.send("No, no, no... {}!".format(message.author.mention))

    else:
        await client.process_commands(message)


@client.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description="Datos del servidor",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue(),
    )
    embed.add_field(
        name="Server created at",
        value=f"{ctx.guild.created_at}".format(ctx.guild.created_at).split(".")[0],
    )
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)


# Comando que recibe como argumento el nombre de una ciudad, comprueba que coincide el usuario que lo solicita
# y devuelve un mensaje con la información de la ciudad
@client.command(pass_context=True)
async def weather(ctx):
    try:
        # Bot pregunta la ciudad
        await ctx.send(f"{ctx.author.mention}, dime una ciudad")
        # Bot espera un mensaje
        msg = await ctx.bot.wait_for(
            "message", check=lambda m: m.author == ctx.author, timeout=10
        )
        # Comprueba que autor del mensaje es el mismo que el que habla el bot
        if msg.author == ctx.author:
            # Guarda el argumento en una variable
            city = msg.content
            weather = weather_module.WeatherModule(city).get_weather()
            temp = weather_module.WeatherModule(city).get_temperature()
            await ctx.channel.send(
                "El tiempo para {} es {} y tienes {}".format(
                    city, weather, temp
                ).upper()
                + "ºC, "
                + f"{ctx.author.mention}"
            )

    except:
        await ctx.send("No, no, no... Eso no.")


client.run(TOKEN)
