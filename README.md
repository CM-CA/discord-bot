# Bot para Discord

Bot de discord diseñado para uso personal y automatizaciones
dentro del servidor.

## Variables de Entorno

El archivo .env debe contener los siguientes parametros con los tokens del usuario

```.env

bot_permissions=
scope_bot=
DISCORD_TOKEN=
OPENWEATHERMAP_API_KEY=

```

Los tokens para el bot se pueden obtener de la siguiente manera [Tutorial Discord]('https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token') y para la API del [Tiempo]('https://openweathermap.org/api').

## Entorno Virtual

Debe crearse un entorno [virtual]('https://docs.python.org/es/3/library/venv.html').

Una vez dentro del entorno virtual, ejecutamos el siguiente comando para instalar las librerias necesarias:

```python
pip install -r requirements.txt
```
