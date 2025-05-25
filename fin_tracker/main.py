import os
from urllib.parse import urljoin

from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv
from flask import Flask, g, request

from fin_tracker.telegram.bot import TelegramBot
from fin_tracker.telegram.router import router

load_dotenv()
BASE_URL = os.getenv("BASE_URL", "")
TELEGRAM_WEBHOOK_UUID = os.getenv("TELEGRAM_WEBHOOK_UUID", "")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")


app = Flask(__name__)

telegram_bot = TelegramBot(TELEGRAM_TOKEN)
telegram_bot.set_webhook(urljoin(BASE_URL, TELEGRAM_WEBHOOK_UUID))
telegram_bot.add_router(router)

@app.before_request
def inject_bot():
    g.telegram_bot = telegram_bot

@app.route(f"/{TELEGRAM_WEBHOOK_UUID}", methods=["POST"])
async def telegram_webhook():
    update = request.get_json()
    await g.telegram_bot.handle_update(update)
    return "OK", 200

asgi_app = WsgiToAsgi(app)
