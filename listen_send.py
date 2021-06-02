import configparser
from telethon import TelegramClient, events
import  asyncio
#get conf from file config.ini
config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
phone = config['Telegram']['phone']
username = config['Telegram']['username']

async def main():
    async with TelegramClient(username, api_id, api_hash) as client:

        @client.on(events.NewMessage(chats='chanell or group to listen'))
        async def my_event_handler(event):
            if str(event).lower().find('word to find ')!= -1:
                receiver2 = await client.get_input_entity('number phone or username to send')
                await client.send_message(receiver2, str(event.raw_text), parse_mode='html')
                print('OK')
        await client.run_until_disconnected()


asyncio.run(main())