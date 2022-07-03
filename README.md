# Bienvenu(e)
C'est quoi Frenchcord?
<br>
Frenchcord est un [api wrapper](https://rapidapi.com/blog/api-glossary/api-wrapper/) de discord api, en python et français.
<br>
Cet api wrapper est open source et optimisé
# Client
Vous allez commencer par créer un client
```py
from frenchcord import Robot
bot = Robot("le token de votre bot")
```
# Command handler
Frenchcord ne donne pas d'evenement de base pour les commandes voici comment creer le handler
```py
@bot.event("message")
def cmd(message):
  bot.process_commands(message)
```
# Commandes
Maintenant vous allez lui appliquer quelques commandes
exemple d'une commande
```py
@bot.command()
def hello_world(ctx):
  ctx.envoyer("Hello world")
```
# Connexion
Maintenant nous allons établir une connexion avec discord
```py
bot.connexion(["?"])
```
Maintenant votre bot est en ligne et prêt à éxécuter des commandes !
