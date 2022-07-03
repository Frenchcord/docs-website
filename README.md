# Bienvenu(e) sur Frenchcord
C'est quoi Frenchcord?
<br>
Frenchcord est un [api wrapper](https://rapidapi.com/blog/api-glossary/api-wrapper/) de discord api, en python et français.
<br>
Cet api wrapper est open source et optimisé
# Commencer
Vous allez commencer par créer un client

```py
from frenchcord import Robot
bot = Robot("le token de votre bot")
```
Maintenant vous allez lui appliquer quelques commandes
exemple d'une commande
```py
@bot.command()
def hello_world(ctx):
  ctx.envoyer("Hello world")
```
Maintenant nous allons établir une connexion avec discord

```py
bot.connexion(["?"])
```
Maintenant votre bot est en ligne et prêt à éxécuter des commandes !
