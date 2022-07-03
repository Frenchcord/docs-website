# Message
## fonctions
```fn
salon, channel {
  description: prend le salon du message,
  args: None,
  return: Le salon du message
}
```

```fn
guild, serveur {
  description: Prend le serveur du message,
  args: None,
  return: Le serveur du message
}
```
## Les attributes
```attribute
id {
  type: snowflake (un Id),
  description: L'id du message
}
```

```attribute
contenu, content {
  type: str (string),
  description: Le contenu du message
}
```

```attribute
type {
  type: int,
  description: le type du message
}
```

```attribute
guild_id, serveur_id {
  type: snowflake (un Id),
  description: L'id du serveur du message
}
```

```attribute
auteur, author {
  type: moitier de un user argument,
  description: auteur du message,
  fonctions: {
    user, utilisateur {
      type: User,
      args: None,
      description: le createur du message (full user)
    }
  }
}
```

```attribute
mention {
  type: array (list) de mentions
  attributes {
    person, human, humain {
      type: moitier de un user argument,
      description: Les personnes mentionners
    }
  }
}
```
