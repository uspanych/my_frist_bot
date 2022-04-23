import configparser
from telethon import TelegramClient


# TODO: вынести В настройки
config = configparser.ConfigParser()
config.read('config.ini')

API_ID = config['Telegram']['api_id']
API_HASH = config['Telegram']['api_hash']
USERNAME = config['Telegram']['username']


def get_client():
    return TelegramClient(USERNAME, API_ID, API_HASH)


async def get_participants(url: str, limit: int = None):
    client = get_client()
    async with client:
        channel = await client.get_entity(url)
        participants = await client.get_participants(channel, limit)
        all_users_details = []
        for participant in participants:
            all_users_details.append({'user_id': participant.id,
                                      'first_name': participant.first_name,
                                      'last_name': participant.last_name,
                                      'username': participant.username,
                                      'phone': participant.phone,
                                      'is_bot': participant.bot})

    return all_users_details
