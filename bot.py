from dotenv import load_dotenv
import os
import discord
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
playlist_id = '6FJJbdmpc1T79OGfXKQQv4'
user_id = '123881475'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

scopes = "playlist-modify-private playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))


@client.event
async def on_ready():
    print('bot logged in and ready to go')


@client.event
async def on_message(message: discord.Message):
    if "open.spotify.com" and "track" in message.content:
        start_index = message.content.index('track') + 6
        end_index = message.content.index('?')
        track_id = message.content[start_index: end_index]
        sp.playlist_add_items(playlist_id, ["spotify:track:" + track_id])

client.run(DISCORD_TOKEN)

