from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import os

TOKEN = os.getenv("7980213474:AAFaU7wUiwFdjNCE2M5w2RAglvsuA8dUdB0
")
CHANNEL = os.getenv("@productsbuild")

bot = Bot(TOKEN)

ofertas = [
    "🔥 Oferta especial del día",
    "💸 Descuento disponible",
    "⚡ Oferta relámpago"
]

contador = 0

def publicar():
    global contador

    bot.send_message(
        chat_id=CHANNEL,
        text=ofertas[contador]
    )

    contador = (contador + 1) % len(ofertas)

scheduler = BlockingScheduler()

scheduler.add_job(publicar, "interval", hours=2)

scheduler.start()
