import asyncio
from pyrogram import Client
from pyrogram.raw.functions.chatlists import CheckChatlistInvite
from pyrogram.raw.types.chatlists import ChatlistInviteAlready

# Данные для Telegram API
API_ID = xxx  # Замени на свой API ID
API_HASH = "xxxxxxx"  # Замени на свой API Hash
SESSION_NAME = "my_session"  # Название сессии
INVITE_SLUG = "H0vPEbCyj3k5YjY6"  # Slug из ссылки


async def get_chatlist():
    async with Client(SESSION_NAME, API_ID, API_HASH) as app:
        try:
            response = await app.invoke(CheckChatlistInvite(slug=INVITE_SLUG))

            if isinstance(response, ChatlistInviteAlready):
                print(f"🔹 ID папки: {response.filter_id}")

                if response.missing_peers:
                    print("\n⚠️ Каналы, которые еще НЕ добавлены:")
                    for peer in response.missing_peers:
                        print(f"- Peer ID: {peer}")

                if response.already_peers:
                    print("\n✅ Каналы, которые уже добавлены:")
                    for peer in response.already_peers:
                        print(f"- Peer ID: {peer}")

                if response.chats:
                    print("\n📌 Подробная информация о каналах:")
                    for chat in response.chats:
                        if chat.username:
                            link = f"https://t.me/{chat.username}"
                        else:
                            link = f"https://t.me/c/{abs(chat.id)}" if str(chat.id).startswith(
                                '-100') else f"ID {chat.id} (нужно проверить вручную)"

                        print(f"- {chat.title} (ID: {chat.id}, Ссылка: {link})")

            else:
                print("❌ Ответ не содержит информации о чатах.")

        except Exception as e:
            print(f"Ошибка: {e}")


# Запуск асинхронной функции
asyncio.run(get_chatlist())
