import random
import discord
from discord.ext import commands
from app.settings import TOKEN
from db.orm import get_session
from db.models import User

bot = commands.Bot(
    command_prefix=">",
    intents=discord.Intents.all()
)

def mitada_session():
    return random.choices([True, False], weights=[5, 95], k=1)[0]

def calculate_aura(mitadas):
    max_mitadas = 100
    return min(1.0, mitadas / max_mitadas)

def update_mitadas_and_aura(author, mitadas_delta):
    author.increment_mitadas(mitadas_delta)
    new_aura = calculate_aura(author.mitadas)
    author.increment_aura(new_aura - author.aura)
    return author.mitadas, author.aura

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    session = get_session()
    author = session.query(User).filter(User.user_id == message.author.id).first()
    if author is None:
        author = User(user_id=message.author.id, aura=0.0, mitadas=0)
        session.add(author)
        session.commit()
        return
    
    if mitada_session():
        mitadas_delta = random.choices([1, -1], weights=[70, 30], k=1)[0]
        new_mitadas, new_aura = update_mitadas_and_aura(author, mitadas_delta)
        session.commit()

        embed = discord.Embed(
            title="Resultado da Mitada" if mitadas_delta > 0 else "Perda de Mitada",
            description=f"Mitadas: {new_mitadas}, Aura: {new_aura * 100:.2f}%",
            color=discord.Color.dark_red()
        )

        if mitadas_delta > 0:
            embed.add_field(
                name="<:carlinhos_imponente:1243614592870121523> Você MITOU!",
                value=f"{message.author.mention} você MITOU!",
                inline=False
            )
        else:
            embed.add_field(
                name="<:honesta_reao:1239690506343026749> Você perdeu uma Mitada",
                value=f"{message.author.mention}, você perdeu uma mitada.",
                inline=False
            )

        await message.channel.send(embed=embed)
    return

def run():
    bot.run(TOKEN)
