# Events
Les events sont des listeners contrairement à discord.py, aucun event de base existe donc pour les commandes il faut faire cela
```py
@bot.event("message")
def cmd(message):
  bot.process_commands(message)
```
Les events sont fait avec des décorateurs
<br>
Voici un exemple
```py
@bot.event("on_ready")
def ptonline():
  print('bot online')
```
Le nom de l'event est ce que on mets dans les arguments des décorateurs
```py
@bot.event("message")
def coucou(message):
  message.envoyer('coucou')
```
Events list
```list
message -> un nouveau message
on_ready -> le bot est en ligne
```
