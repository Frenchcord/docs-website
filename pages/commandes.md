# Commandes
Les commandes sont fait avec des décorateurs
<br>
Voici un exemple
```py
@bot.command()
def commande(ctx):
  pass
```
Le nom de la fonction est le nom de la commande par exemple<br>
Le nom de la commande est : "coucou"
La commande envoie le mot "coucou"
```py
@bot.command()
def coucou(ctx):
  ctx.envoyer('coucou')
```
