# Context
## Les attributes
```attribute
message {
  type: Message,
  description: Le message qui s'est fait envoyer
}
```

```attribute
salon, channel {
  type: snowflake (un Id),
  description: L'id du salon que le message s'est fait poster dedans
}
```

```attribute
salon_id, channel_id {
  type: snowflake (un Id),
  description: L'id du salon que le message s'est fait poster dedans
}
```

```attribute
guild_id, serveur_id {
  type: snowflake (un Id),
  description: L'id du serveur que le message s'est fait poster dedans
}
```
## Les fonctions

```fn
serveur, guild {
  args: none,
  description: retourne le salon,
  return: Le serveur que le message s'est fait poster dedans
}
```

```fn
send, envoyer {
  description: Envoie un message discord dans le salon du contexte,
  args: [contenu, embeds, data]
  args: {
    contenu {
      optional: True,
      type: str (string),
      max-size: 4000,
      description: Le contenu, que vous voulez envoyer dans votre message
    },
    embeds {
      optional: True,
      type: array (list),
      type-de-valeur-dans-la-liste: Discord-embed,
      description: Des discord embeds, que vous voulez envoyer dans votre message
    },
    data {
      optional: True,
      type: bool (boointegerlean),
      defaut: True,
      description: Est ce que la fonction va retourner quelque chose?
    }
  },
  return: Message if data is True else None
}
```
