from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler , MessageHandler, filters
from parsers import get_data
import asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="izmantojiet /today, lai iegutu sodienas grafiku.")

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loop = asyncio.get_event_loop()

    times, titles = await loop.run_in_executor(None, get_data)
    if times:
        for i in range(len(times)):
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{times[i]} \n {titles[i]}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"brivdiena")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="neesosa komanda")

if __name__ == '__main__':
    application = ApplicationBuilder().token('token').build()
    
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    start_handler = CommandHandler('start', start)
    today_handler = CommandHandler('today', today)
    application.add_handler(start_handler)
    application.add_handler(today_handler)
    application.add_handler(unknown_handler)

    
    application.run_polling()