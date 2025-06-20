import os
import socket
from discord.ext import commands, tasks
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
ip = os.getenv("SERVER_IP")
intents = discord.Intents.default()
intents.message_content = True
# ici j'utilise le command_prefix pour de futures commandes, si c'est juste pour le ping
# n'en tenez pas compte
client = commands.Bot(command_prefix='$', intents=intents)

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Toutes les 60 secondes un ping sera envoyé
INTERVAL = 60


@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")
    # Loop pour envoyer les pings, toutes les minutes par défaut
    send_message_loop.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        # Utile pour voir si le bot fonctionne de temps en temps
        # Mais remplacez pour ce que vous voulez, ou même supprimez
        if '$test' in message.content:
            user_id = message.author.id
            user = await client.fetch_user(user_id)
            await message.channel.send(f"{user.mention}, attention ! ⚠️ \n Tu as envoyé la commande test !")


@tasks.loop(seconds=INTERVAL)
async def send_message_loop():
    channel = client.get_channel(CHANNEL_ID)
    # On pourrait mettre une liste d'id, et parcourir ces id pour que chacun soit tag
    # si il y a plusieurs admins, ou personnes qui doivent être au courant
    user_id = 000000000000 # Passer votre UserID ici pour être tag

    user = await client.fetch_user(user_id)

    if channel:
        True if check_port(ip, 80) else await channel.send(f"{user.mention}Port 80 down")
        True if check_port(ip, 443) else await channel.send(f"{user.mention}Port 443 down")
    else:
        print("Salon introuvable.")


def check_port(ip, port, timeout=3):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        return result == 0



client.run(TOKEN)




