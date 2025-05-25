from aiogram import Bot, Dispatcher, Router
from aiogram.types import Update
from requests import post


class TelegramBot:
    def __init__(self, token: str):
        self.bot = Bot(token=token)
        self.dispatcher = Dispatcher()

    async def handle_update(self, update: Update):
        update = Update.model_validate(
            update,
            context={"bot": self.bot},
        )
        await self.dispatcher.feed_update(self.bot, update)

    def add_router(self, router: Router):
        self.dispatcher.include_router(router)

    def set_webhook(self, webhook_url: str):
        response = post(
            f"https://api.telegram.org/bot{self.bot.token}/setWebhook",
            data={"url": webhook_url},
        )
        print(response.json())
